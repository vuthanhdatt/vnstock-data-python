import os
import io
import ast
import requests
import configparser
import pandas as pd
from dotenv import load_dotenv


#Load session id for testing
load_dotenv()
PHPSESSID = ast.literal_eval(os.getenv('PHPSESSID'))

#Load url
cfg = configparser.ConfigParser()
cfg.read('config.ini')
price_url = cfg['data']['price']


def price_data(ticket, cookies, start, end):
    '''
    Return price data of company or list companies in date range
    -------------
    ticket: str or list
    cookies: dict
    start: str or datetime
    end: str or datetime
    '''
    result = None

    if isinstance(ticket, str):

        r  = requests.get(price_url+ticket, cookies=cookies, verify=False)
        content = r.content.decode('utf8')
        df = pd.read_csv(io.StringIO(content))
        if len(df) != 0:
            df.columns = ['Ticket','Date','Open','High','Low','Close','Volume']
            df.set_index('Date', inplace=True)
            df.index =pd.to_datetime(df.index, format='%Y%m%d')
        else:
            raise ValueError('Wrong ticket')
        result = df.loc[start:end,:]

    elif isinstance(ticket, list):
        df_list = []
        for t in ticket:
            df = price_data(t, cookies, start, end)
            df_list.append(df)
        df = pd.concat(df_list)
        result=df.groupby(['Ticket',df.index]).sum()
        
    else:
        raise TypeError("Ticket must be a string or list of string")

    return result
    

if __name__ == '__main__':
    # print(price_url)
    print(price_data('UAE', PHPSESSID, '13-5-2021','31-10-2021'))
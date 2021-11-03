import os
import ast
import requests
import configparser
import pandas as pd
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from helpers.data_helper import *

#Load tokens for testing
load_dotenv()
cookies = ast.literal_eval(os.getenv('COOKIES'))

#Load config data
cfg = configparser.ConfigParser()
cfg.read('vnstock_data\config.ini')

headers = ast.literal_eval(cfg['request']['header'])
market_index_url = cfg['data']['market_index']



def get_market_index_history(exchange, start, end, cookies,type='basic', **kwargs):

    params = market_index_params(exchange,start,end)
    r = requests.get(market_index_url, headers=headers, cookies=cookies, params=params)
    content = r.content
    result = read_market_index_file(content)

    return result



# def price_data(ticket, cookies, start, end):
#     '''
#     Return price data of company or list companies in date range.
#     ---------------------
#     ticket: str or list
#     cookies: dict
#     start: str or datetime
#     end: str or datetime
#     '''
#     result = None

#     if isinstance(ticket, str):

#         r  = requests.get(price_url+ticket, cookies=cookies, verify=False)
#         content = r.content.decode('utf8')
#         df = pd.read_csv(io.StringIO(content))
#         if len(df) != 0:
#             df.columns = ['Ticket','Date','Open','High','Low','Close','Volume']
#             df.set_index('Date', inplace=True)
#             df.index =pd.to_datetime(df.index, format='%Y%m%d')
#         else:
#             raise ValueError('Wrong ticket')
#         result = df.loc[start:end,:]

#     elif isinstance(ticket, list):
#         df_list = []
#         for t in ticket:
#             df = price_data(t, cookies, start, end)
#             df_list.append(df)
#         df = pd.concat(df_list)
#         result=df.groupby(['Ticket',df.index]).sum()
        
#     else:
#         raise TypeError("Ticket must be a string or list of string")

#     return result
    

if __name__ == '__main__':
    print(get_market_index_history('hnx','2020-01-04','2021-07-02', cookies= cookies))
    

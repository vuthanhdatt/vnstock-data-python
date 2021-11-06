import io
import ast
import configparser
import pandas as pd


#Load url and headers
cfg = configparser.ConfigParser()
cfg.read('vnstock_data\config.ini')

headers = ast.literal_eval(cfg['request']['header'])
market_index_url = cfg['price']['market_index']
price_hisory_url = cfg['price']['price_history']


############helper for market index#################
def market_index_params(exchange,start, end):
    params = {'fromDate': start,
                'toDate': end}
    if exchange == 'hose':
        params['catID'] = '1'
        params['stockID'] = '-19'
    elif exchange == 'hnx':
        params['catID'] = '2'
        params['stockID'] = '-18'
    else:
        params['catID'] = '3'
        params['stockID'] = '-17'
    return params

def read_market_index_file(content):
    df = pd.read_excel(io.BytesIO(content), skiprows=7)
    df = df.iloc[:,[2,4,5,6,7,8,-3,-1]][1:]
    df.columns = ['Date','PreClose', 'Open','Close','High','Low','Volume','MarketCap']
    df = df.set_index('Date')
    return df

#########helper for get price history###############

def make_price_history_form(symbol,start, end):
    form = {'Code': symbol,
            'OrderBy':'', 
            'OrderDirection': 'desc',
            'FromDate': start,
            'ToDate': end,
            'ExportType': 'excel',
            'Cols': 'MC,DC,CN,TN,GYG,BQ,GDC,TKLGD',
            'ExchangeID': 1}
    return form
    
def make_price_history_df(df):
    col = ['Date','Volume','Open','Close', 'High','Low','High-Low','Average','Adj Close']
    df.columns = col
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    df = df.reindex(['High','Low','Open', 'Close','Volume','Adj Close','Average','High-Low'], axis='columns')
    return df




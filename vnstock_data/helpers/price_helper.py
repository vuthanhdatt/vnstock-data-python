import io
import ast
import configparser
import pandas as pd


# Load url and headers
cfg = configparser.ConfigParser()
cfg.read('vnstock_data\config.ini')

headers = ast.literal_eval(cfg['request']['header'])
market_index_url = cfg['price']['market_index']
price_hisory_url = cfg['price']['price_history']


############helper for market index#################
def market_index_params(exchange, start, end):
    '''
    Make paramaters for request to market_index_url.

    Paramaters
    ----------
    exchange: string, name of stock exchange, etc. hose, hnx...
    start: string, starting date.
    end: string, ending date.

    Return: 
    -------
    dict
    '''

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
    '''
    Reading binary file to complete DataFrame.
    Since calling requests to market_index_url return response not in excel file,
    this fuction help convert to DataFrame and modify to right format.

    Paramaters
    ----------
    content: binary, response of request to market_index_url.

    Return: 
    ----------
    DataFrame

    '''

    df = pd.read_excel(io.BytesIO(content), skiprows=7)
    df = df.iloc[:, [2, 4, 5, 6, 7, 8, 11, -3, -1]][1:]
    df.columns = ['Date', 'PreClose', 'Open',
                  'Close', 'High', 'Low','Change(%)' ,'Volume', 'MarketCap']
    df = df.set_index('Date')

    return df

#############helper for get price history###############


def make_price_history_form(symbol, start, end):
    '''
    Making form to requests to market_price_url

    Paramaters
    ----------
    symbol: string, company symbol
    start: starting date
    end: ending date

    Retruns
    -------
    dict
    '''

    form = {'Code': symbol,
            'OrderBy': '',
            'OrderDirection': 'desc',
            'FromDate': start,
            'ToDate': end,
            'ExportType': 'excel',
            'Cols': 'MC,DC,CN,TN,GYG,BQ,GDC,TKLGD',
            'ExchangeID': 1}

    return form


def make_price_history_df(df):
    '''
    Formating price df 

    Paramaters
    ----------
    df: DataFrame, df reading from price_history_url

    Return
    ------
    DataFrame

    '''
    cols = ['Date', 'Volume', 'Open', 'Close', 'High',
           'Low', 'High-Low', 'Average', 'Adj Close']
    df.columns = cols
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    df = df.reindex(['High', 'Low', 'Open', 'Close', 'Volume',
                    'Adj Close', 'Average', 'High-Low'], axis='columns')
                    
    return df

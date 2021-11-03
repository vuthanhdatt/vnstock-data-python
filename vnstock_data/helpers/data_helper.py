import io
import pandas as pd


#helper for market index
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
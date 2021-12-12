import requests
from vnstock_data.helpers.price_helper import *


def get_market_index_history(exchange, start, end, cookies):

    '''
    Take market index of specific exchange from start to end, coming with user cookies.

    Paramaters
    ----------
    exchange: string, stock exchange name, etc. hose, hnx...
    start: string, starting date
    end: string, ending date
    cookies: dict, user cookies

    Return
    ------
    DataFrame
    '''

    params = market_index_params(exchange,start,end)
    r = requests.get(market_index_url, headers=headers, cookies=cookies, params=params)
    content = r.content
    result = read_market_index_file(content)

    return result


def get_price_history(symbol,start,end, cookies):

    '''
    Take price history of specific company from start to end, coming with user cookies.

    Paramaters
    ----------
    symbol: string, company symbol, etc. 'fts', 'hpg'...
    start: string, starting date
    end: string, ending date
    cookies: dict, user cookies
    
    Return
    ------
    DataFrame
    '''

    form = make_price_history_form(symbol,start,end)
    r = requests.get(price_history_url, headers= headers, data=form, cookies= cookies)
    df = pd.read_html(r.text)[1]
    result = make_price_history_df(df)
    
    return result
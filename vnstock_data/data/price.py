import requests
from helpers.price_helper import *


def get_market_index_history(exchange, start, end, cookies,type='basic', **kwargs):
    
    params = market_index_params(exchange,start,end)
    r = requests.get(market_index_url, headers=headers, cookies=cookies, params=params)
    content = r.content
    result = read_market_index_file(content)

    return result


def get_price_history(symbol,start,end, cookies):

    form = make_price_history_form(symbol,start,end)
    r = requests.get(price_hisory_url, headers= headers, data=form, cookies= cookies)
    df = pd.read_html(r.text)[1]
    result = make_price_history_df(df)
    
    return result
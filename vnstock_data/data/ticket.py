import requests
from helpers.ticket_helper import *


def get_all_com(exchange, cookies, industry= 'all', b_type='all', basic=True):
    '''
    Return all companies on choosen exchange.

    Paramaters
    __________
    exchange: string, stock exchange name, etc. hose, hnx...
    cookies: dict, user cookies
    industry: string, industry id in :func:`~main.VnStock.industry_type`
    b_type: string, business code in :func:`~main.VnStock.business_type`
    basic: boolen,

    Return
    ------
    DataFrame
    
    '''
    token = get_all_com_token(cookies)
    b_df = get_business_type(cookies=cookies)
    page = 1
    r_list = []
    while True:
        f = make_all_com_form(exchange,industry, b_type, token,page,b_df)
        r = requests.post(company_list_url, headers=headers,cookies=cookies,data=f)
        if len(r.json()) != 0:
            r_list.append(r.json())
            page +=1
        else:
            break
    df = concat_df(r_list)
    if basic:
        result = df.loc[:,['Exchange','Code']].reindex(columns=['Code','Exchange'])
    else:
        result = df.loc[:,['Exchange','Code','Name','IndustryName','TotalShares']].reindex(columns=['Code','Name','IndustryName','TotalShares','Exchange'])
    return result



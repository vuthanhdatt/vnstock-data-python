import requests
from helpers.financeinfo_helper import *

######## Update bussiness result ###########

def update_finance_result(cookies, industry='all'):
    '''
    Return up to date finance result of current quarter

    Paramaters
    ----------
    cookies: dict, user cookies
    industry: string, industry id in :func:`~main.VnStock.industry_type`
    
    Return
    ______
    DataFrame
    '''

    token = get_update_result_token(cookies)
    f = make_update_result_form(token, industry)
    r = requests.post(update_result_url, headers=headers, cookies=cookies, data=f)
    content = r.json()
    result = build_df_update_result(content)
    return result
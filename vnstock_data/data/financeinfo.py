import requests
from vnstock_data.helpers.financeinfo_helper import *

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
    token_url = 'https://finance.vietstock.vn/ket-qua-kinh-doanh'
    token = get_token(cookies, token_url)
    f = make_update_result_form(token, industry)
    r = requests.post(update_result_url, headers=headers, cookies=cookies, data=f)
    content = r.json()
    result = build_df_update_result(content)
    return result
    

###################### RATIOS ########################

def get_ratios(cookies, symbol, yearly= True):
    '''
    Return companies's financial ratios in history.

    Paramaters
    ----------
    cookies: dict, user cookies
    symbol: string, company code
    yearly: boolen, if False return result in quarterly

    Return
    ------
    DataFrame
    '''

    df_list = []
    page = 1
    token_url = 'https://finance.vietstock.vn/AAA/financials.htm?tab=CSTC'
    token = get_token(cookies, token_url)
    while True:       
        form = make_finance_info_form(symbol,page,token, 'CSTC',yearly)
        r = requests.post(finance_info_url, cookies=cookies, headers=headers, data= form)
        content = r.json()
        if len(content[0]) != 0:
            df_list.append(buid_ratios_df(content,yearly))
            page+=1
        else:
            break
        df = pd.concat(df_list[::-1], axis=1, join="inner")
        result = df.loc[:,~df.columns.duplicated()]
    return result

############# CONDENSED BS ######################

def get_condensed_bs(cookies, symbol, yearly= True):
    '''
    Return companies's condensed balance sheet in history.

    Paramaters
    ----------
    cookies: dict, user cookies
    symbol: string, company code
    yearly: boolen, if False return result in quarterly

    Return
    ------
    DataFrame
    '''
    df_list = []
    page = 1
    token_url = 'https://finance.vietstock.vn/AAA/financials.htm?tab=CSTC'
    token = get_token(cookies, token_url)
    while True:       
        form = make_finance_info_form(symbol,page,token,'BCTT', yearly)
        r = requests.post(finance_info_url, cookies=cookies, headers=headers, data= form)
        content = r.json()
        if len(content[0]) != 0:
            df_list.append(build_condensed_bs_df(content,yearly))
            page+=1
        else:
            break
        df = pd.concat(df_list[::-1], axis=1, join="inner")
        result = df.loc[:,~df.columns.duplicated()]
    return result
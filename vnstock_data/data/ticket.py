import requests
from helpers.ticket_helper import *


def get_all_com(exchange, cookies, industry= 'all', b_type='all', basic=True):
    token = get_token(cookies)
    b_df = get_bussiness_type()
    page = 1
    r_list = []
    while True:
        f = make_form(exchange,industry, b_type, token,page,b_df)
        r = requests.post(company_list_url, headers=headers,cookies=cookies,data=f)
        if len(r.json()) != 0:
            r_list.append(r.json())
            page +=1
        else:
            break
    df = concat_df(r_list)
    if basic == True:
        result = df.loc[:,['Exchange','Code']].reindex(columns=['Code','Exchange'])
    else:
        result = df.loc[:,['Exchange','Code','Name','IndustryName','TotalShares']].reindex(columns=['Code','Name','IndustryName','TotalShares','Exchange'])
    return result



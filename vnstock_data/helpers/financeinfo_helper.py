import ast
import requests
import configparser
import pandas as pd
from bs4 import BeautifulSoup


#Load url
cfg = configparser.ConfigParser()
cfg.read('vnstock_data\config.ini')

update_result_url = cfg['financeinfo']['update_finance_result']
headers = ast.literal_eval(cfg['request']['header'])


########## Helper for update finance result ###########

def get_update_result_token(cookies):
    '''
    Get token of session to put in form

    '''
    sess = requests.Session()
    url = 'https://finance.vietstock.vn/ket-qua-kinh-doanh'
    r= sess.get(url,headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.content, 'html5lib')
    token = soup.findAll('input', attrs={'name':'__RequestVerificationToken'})[0]['value']
    return token

def make_update_result_form(token,industry_id='all'):
    '''
    Make form to request to api

    '''
    if industry_id =='all':
        industry_id = '0'
    f = {'catID': '0',
        'industryID': industry_id,
        'code': '',
        'order': '',
        '__RequestVerificationToken':token}
    return f

def build_df_update_result(content):
    '''
    Turn raw df from response to proper format

    '''
    df = pd.DataFrame(content)
    col = ['StockCode','INDEX','NetProfit','Profit_DiffPreviousTerm','Profit_DiffSameTerm','Profit_Accumulated','EPS','EPS_Accumulated','PE','BVPS','NetRevenue']
    result = df.loc[:,col]
    result.columns = ['Symbol','Exchange','NetProfit','Profit_DiffPreviousTerm(%)','Profit_DiffSameTerm(%)','Profit_Accumulated','EPS','EPS_Accumulated','P/E','BVPS','NetRevenue']
    result = result.reindex(columns=['Symbol','NetProfit','Profit_DiffPreviousTerm(%)','Profit_DiffSameTerm(%)','Profit_Accumulated','EPS','EPS_Accumulated','P/E','BVPS','NetRevenue','Exchange'])
    return result

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
    load_dotenv('vnstock_data\.env')
    cookies = ast.literal_eval(os.getenv('COOKIES'))
    print(get_update_result_token(cookies))
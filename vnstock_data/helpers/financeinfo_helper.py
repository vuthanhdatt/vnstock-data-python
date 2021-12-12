import requests
import pandas as pd
from bs4 import BeautifulSoup


#Load url


update_result_url= 'https://finance.vietstock.vn/data/allkqkdorder'
finance_info_url = 'https://finance.vietstock.vn/data/financeinfo'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40'}


############ get token #####################
def get_token(cookies, url):
    sess = requests.Session()
    r= sess.get(url,headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.content, 'html5lib')
    token = soup.findAll('input', attrs={'name':'__RequestVerificationToken'})[0]['value']
    return token


########## Helper for update finance result ###########

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

################## RATIOS ##############

def make_ratio_form(symbol, page,token, yearly= True):
    
    '''
    Making form request to api
    '''
    f = {
        'Code': symbol,
        'ReportType': 'CSTC',
        'Unit': '1000000000',
        'Page': str(page),
        'PageSize': '4',
        '__RequestVerificationToken': token
    }

    if yearly:
        f['ReportTermType'] = '1'
    else:
        f['ReportTermType'] = '2'
    return f

def buid_ratios_df(content, yearly):

    '''
    Help building df from raw response when request. 
    '''
    index = []
    df_dict = {}
    if yearly:
        year = [str(content[0][i]['YearPeriod']) for i in range(len(content[0]))]
    else:
        year = [content[0][i]['TermCode'] + '/' + str(content[0][i]['YearPeriod']) for i in range(len(content[0]))]
    for y in year[::-1]:
        df_dict[y] = []
    for k, v in content[1].items():
        for value in v:
            for i in range(4):
                df_dict[year[::-1][i]].append(value[f'Value{i+1}'])
            index.append((k,value['NameEn']))
    df_dict = dict(reversed(list(df_dict.items())))
    id = pd.MultiIndex.from_tuples(index, names=["Type", "Ratios"])
    df = pd.DataFrame(df_dict, index=id)
    result = df.loc[~df.index.duplicated(keep='first')]

    return result






if __name__ == '__main__':
    pass
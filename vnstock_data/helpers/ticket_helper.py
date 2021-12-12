import requests
import pandas as pd
from bs4 import BeautifulSoup


#Load url

company_list_url = 'https://finance.vietstock.vn/data/corporateaz'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40'}



###### Helper for get_all_com() ########
def get_business_type(cookies):
    '''
    Take all business type 
    '''
    url = 'https://finance.vietstock.vn/data/businesstype'
    r = requests.get(url, headers=headers, cookies=cookies)
    business_alias = ['JSC','IC','SC','B','FC','OFI','FMC','AC']
    df = pd.DataFrame(r.json())
    df['Code'] = business_alias
    df = df.set_index('ID')
    df.rename(columns={'Title':'Name'}, inplace=True)
    return df

def get_industry_list(cookies):
    '''
    Take all industry type
    '''
    url = 'https://finance.vietstock.vn/data/industrylist'
    r = requests.get(url, headers=headers,cookies=cookies)
    r = pd.DataFrame(r.json())
    r = r.set_index('ID')
    return r

def get_all_com_token(cookies):
    '''
    Get token session to make request to api
    '''
    sess = requests.Session()
    url = 'https://finance.vietstock.vn/doanh-nghiep-a-z?page=1'
    r= sess.get(url,headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.content, 'html5lib')
    token = soup.findAll('input', attrs={'name':'__RequestVerificationToken'})[0]['value']
    return token


def make_all_com_form(exchange, industry_id, b_type, token, page, bussines_df):
    '''
    Make form to call to api
    '''
    catID = {'all': '0' ,'hose':'1','hnx':'2','upcom':'5'}
    if b_type == 'all':
        b_ID = '0'
    else:
        b_ID = str(bussines_df[bussines_df['Code'] == b_type].index.values[0])
    if industry_id =='all':
        industry_id = '0'
 
    f = {'catID': catID[exchange],
    'industryID': industry_id,
    'page':page,
    'pageSize': '50',
    'code':'',
    'businessTypeID':b_ID,
    'orderBy': 'Code',
    'orderDir': 'ASC',
    '__RequestVerificationToken':token}
    return f

def concat_df(r_list):
    '''
    Due to each response only return 50 companies. We will call multi request, this fucntion help concat
    response of each request to one final df
    '''
    df_list = [] 
    for r in r_list:
        df_list.append(pd.DataFrame(r))
    result = pd.concat(df_list)
    result.reset_index(drop=True, inplace=True)
    return result


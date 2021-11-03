import ast
import requests
import configparser
import pandas as pd
from pandas.core.frame import DataFrame

#Load url
cfg = configparser.ConfigParser()
cfg.read('vnstock-data\config.ini')
company_list_url = cfg['ticket']['company_list']

def load_company() -> DataFrame:

    company_list = []
    r = requests.get(company_list_url, verify=False)
    raw_response = r.text
    response = raw_response.replace('var companyinfo = ','').replace("stockname","'stockname'").replace("companyname","'companyname'")

    response_list = response.split(',\n')
    response_list[0] =response_list[0].replace('[','')
    response_list[-1] = response_list[-1].replace('];','')

    for com in response_list:
        company_list.append(ast.literal_eval(com))
    df = pd.DataFrame(company_list)
    df.columns = ['Ticket','Name']
    return df

def company_ticket() -> DataFrame:
    '''
    Return all com
    '''
    df = load_company()
    df = df[df['Ticket'].str.len() == 3]
    df = df[~df['Ticket'].str.contains("^", regex=False)]
    return df
# for com in company_list:
#     ticket.append(com['stockname'])
#     company_name.append(com['companyname'])


if __name__ == '__main__':
    print(company_ticket())
    # print(company_list_url)

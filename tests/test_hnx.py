import os
import ast
import sys
from dotenv import load_dotenv
sys.path.append('vnstock_data')
from hnx import Hnx

#Load cookies for testing
load_dotenv()
cookies = ast.literal_eval(os.getenv('COOKIES'))
start = '2021-04-04'
end = '2021-11-01'

if __name__ == '__main__':
    hnx = Hnx(cookies)
    print(hnx.market_index(start, end))
    # print(hnx.all_company_info())
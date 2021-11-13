import os
import ast
import sys

sys.path.append('vnstock_data')
from dotenv import load_dotenv
from data.financeinfo import *

#Load cookies for testing
load_dotenv('vnstock_data\.env')
cookies = ast.literal_eval(os.getenv('COOKIES'))

class TestFinanceinfo:
    def test_update_business_result(self):
        check = update_finance_result(cookies,'300')
        check = check[check['Symbol'] == 'GAS']
        assert check['P/E'].values == 26.9 


if __name__ == '__main__':
    print(update_finance_result(cookies,'300'))


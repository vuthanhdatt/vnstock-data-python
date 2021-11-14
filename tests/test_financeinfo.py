import os
import ast
import sys
import pytest

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

    def test_get_ratios(self):
        check = get_ratios(cookies,'AAA',True)
        assert check.loc[:,'2020'][4] == 0.43
        


if __name__ == '__main__':
    print(update_finance_result(cookies,'300'))


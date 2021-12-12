import os
import ast
import sys

sys.path.append('vnstock_data')
from dotenv import load_dotenv
from data.price import *

#Load cookies for testing
load_dotenv('vnstock_data\.env')
cookies = ast.literal_eval(os.getenv('COOKIES'))

class TestPrice:
    def test_get_price_history(self):
        check = get_price_history('FTS','07-07-2021','11-5-2021',cookies)
        assert int(check.loc['7-13-2021','High'].values) == 34500

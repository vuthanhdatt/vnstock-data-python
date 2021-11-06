import os
import ast
import sys


sys.path.append('vnstock_data')
from main import VnStock
from hnx import Hnx
from hose import Hose
from upcom import UpCom
from dotenv import load_dotenv



#Load cookies for testing
load_dotenv('vnstock_data\.env')
cookies = ast.literal_eval(os.getenv('COOKIES'))

########TEST MAIN CLASS############

vndata = VnStock(cookies)

class TestMain:

    def test_bussiness_type(self):
        assert len(vndata.bussiness_type) == 8
    
    def test_industry_type(self):
        assert len(vndata.industry_type) == 20

    def test_price(self):
        check = vndata.price('HPG','8-8-2021','11-5-2021')
        assert int(check.loc['8-10-2021','Low'].values) == 49100
        assert check.shape == (63,8)


##########TEST HNX CLASS###########

hnx = Hnx(cookies)

class TestHnx:
    
    def test_company_info(self):
        df = hnx.all_company_info('200', 'all')
        check = df.iloc[5,0]
        assert check == 'HPM'
        assert len(df) == 20



##########TEST HOSE CLASS###########

hose = Hose(cookies)

class TestHose:
    
    def test_company_info(self):
        df = hose.all_company_info('1000', 'all')
        check = df.iloc[11,0]
        assert check == 'EIB'
        assert len(df) == 48

#########TEST UPCOM CLASS###############

upcom = UpCom(cookies)

class TestUpcom:
    
    def test_company_info(self):
        df = upcom.all_company_info('1500', 'all')
        check = df.iloc[1,0]
        assert check == 'SRB'
        assert len(df) == 2

if __name__ == '__main__':
    pass
    
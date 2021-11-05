import os
import ast
import sys

sys.path.append('vnstock_data')
from main import VnStock
from hnx import Hnx
from hose import Hose
from upcom import UpCom
from dotenv import load_dotenv, main



#Load cookies for testing
load_dotenv()
cookies = ast.literal_eval(os.getenv('COOKIES'))

########TEST MAIN CLASS############

vndata = VnStock(cookies)

class TestMain:
    def test_bussiness_type(self):
        assert len(vndata.bussiness_type) == 8
    
    def test_industry_type(self):
        assert len(vndata.industry_type) == 20

import os
import ast
import sys


sys.path.append('vnstock_data')
from main import VnStock
from hnx import Hnx
from hose import Hose
from upcom import UpCom
from dotenv import load_dotenv


# Load cookies for testing
load_dotenv('vnstock_data\.env')
cookies = ast.literal_eval(os.getenv('COOKIES'))
start = '8-8-2021'
end = '11-5-2021'

########TEST MAIN CLASS############

vndata = VnStock(cookies)


class TestMain:

    def test_business_type(self):
        assert len(vndata.business_type) == 8

    def test_industry_type(self):
        assert len(vndata.industry_type) == 20

    def test_price(self):
        check = vndata.price('HPG', start, end)
        assert int(check.loc['8-10-2021', 'Low'].values) == 49100
        assert check.shape == (63, 8)

        check = vndata.update_finance_result('900')
        check = check[check['Symbol'] == 'FPT']
        assert int(check['NetProfit'].values) == 1124

##########TEST HNX CLASS###########


hnx = Hnx(cookies)


class TestHnx:

    def test_company_info(self):
        df = hnx.all_company_info('200', 'all')
        check = df.iloc[5, 0]
        assert check == 'HPM'
        assert len(df) == 20

    def test_market_index(self):
        check = hnx.market_index(start, end)
        assert check.loc['18-10-2021', 'Open'].values == 384.84


##########TEST HOSE CLASS###########

hose = Hose(cookies)


class TestHose:

    def test_company_info(self):
        df = hose.all_company_info('1000', 'all')
        check = df.iloc[11, 0]
        assert check == 'EIB'
        assert len(df) == 48

    def test_market_index(self):
        check = hose.market_index(start, end)
        assert check.loc['21-10-2021', 'Low'].values == 1384.77


#########TEST UPCOM CLASS###############

upcom = UpCom(cookies)


class TestUpcom:

    def test_company_info(self):
        df = upcom.all_company_info('1500', 'all')
        check = df.iloc[1, 0]
        assert check == 'SRB'
        assert len(df) == 2

    def test_market_index(self):
        check = upcom.market_index(start, end)
        assert check.loc['13-10-2021', 'Open'].values == 98.81

from datetime import datetime
if __name__ == '__main__':
    # start=datetime.now()
    # df = hnx.all_company_info()
    # l = df['Code'].tolist()
    # with open(r'C:\Users\Milky\OneDrive - VNU-HCMUS\Kinh doanh\STOCK MARKET\python-ta\data\hnx\hnx.txt', 'w') as f:
    #     for item in l:
    #         f.write( item + ',')
    # # my_file = open(r"C:\Users\Milky\OneDrive - VNU-HCMUS\Kinh doanh\STOCK MARKET\python-ta\data\hose.txt", "r")
    # # content = my_file.read()
    # # com = content.split(',')
    # # for c in com:
    # #     df = vndata.price(c,'01-01-2000','11-18-2021')
    # #     df.to_csv(f'C:\\Users\\Milky\\OneDrive - VNU-HCMUS\\Kinh doanh\\STOCK MARKET\\python-ta\\data\\hose\\{c}.csv',index=True)
    # print(datetime.now()-start)
    pass
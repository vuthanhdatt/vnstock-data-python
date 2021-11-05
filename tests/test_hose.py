import os
import ast
import sys
from dotenv import load_dotenv
sys.path.append('vnstock_data')
from hose import Hose

#Load cookies for testing
load_dotenv()
cookies = ast.literal_eval(os.getenv('COOKIES'))

if __name__ == '__main__':
    hose = Hose(cookies)
    print(hose.all_company_info())


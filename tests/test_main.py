from datetime import datetime
import os
import ast
import sys
from dotenv import load_dotenv
sys.path.append('vnstock_data')
from main import VnStock

#Load cookies for testing
load_dotenv()
cookies = ast.literal_eval(os.getenv('COOKIES'))

if __name__ == '__main__':
    start = datetime.now()
    vn = VnStock(cookies)
    print(vn.industry_type)
    print(datetime.now()-start)
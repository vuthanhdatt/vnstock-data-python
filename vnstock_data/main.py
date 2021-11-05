import data.price as price
import data.ticket as ticket
from base import BaseStock

class VnStock(BaseStock):
    def __init__(self, cookies:dict) -> None:
        super().__init__()
        self.__cookies = cookies
        self.exchange = 'all'
    
    @property
    def bussiness_type(self):
        return ticket.get_bussiness_type()

    @property
    def industry_type(self):
        return ticket.get_industry_list()

    def all_company_info(self, industry_type='all', bussines_type='all', basic=True):
        return  ticket.get_all_com(self.exchange, self.__cookies, industry=industry_type, b_type=bussines_type,basic=basic)
       



    
    

import data.price as price
import data.ticket as ticket
from base import BaseStock

class UpCom(BaseStock):
    def __init__(self, cookies) -> None:
        super().__init__()
        self.__cookies = cookies
        self.exchange = 'upcom'

    def market_index(self, start, end, type='basic', **kwargs):
        return price.get_market_index_history(self.exchange,start, end,cookies=self.__cookies, type=type)

     
    def all_company_info(self, industry_type='all', bussines_type='all', basic=True):
        com_info = ticket.get_all_com(self.exchange, self.__cookies, industry=industry_type, b_type=bussines_type,basic=basic)
        com_info.drop('Exchange',axis=1,inplace=True)
        return com_info
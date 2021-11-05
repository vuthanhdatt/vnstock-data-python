from abc import ABC, abstractmethod

class BaseStock(ABC):
    
    @property
    def current_market_index(self):
        pass
    
    @staticmethod
    def market_index(self,start,end,type='basic',**kwargs):
        pass
    @abstractmethod
    def all_company_info(self, industry_type, bussiness_type, basic=True):
        pass
from abc import ABC, abstractmethod

class BaseStock(ABC):
    
    # @property
    # @abstractmethod
    # def current_market_index(self):
    #     pass
    
    @abstractmethod
    def market_index(self,start,end,type='basic',**kwargs):
        pass
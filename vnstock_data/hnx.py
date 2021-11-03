from base import BaseStock
from data import get_market_index_history

class Hnx(BaseStock):
    def __init__(self, cookies) -> None:
        super().__init__()
        self.__cookies = cookies
        self.exchange = 'hnx'

    def market_index(self, start, end, type='basic', **kwargs):
        return get_market_index_history(self.exchange,start, end,cookies=self.__cookies, type=type)

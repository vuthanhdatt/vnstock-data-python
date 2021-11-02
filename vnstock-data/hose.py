import configparser
from base import BaseStock
from data import get_market_index_history


class Hose(BaseStock):
    def market_index(self, start, end, type='basic', exchange='hose', **kwargs):
        return get_market_index_history(exchange,start, end, type=type)

if __name__ == '__main__':
    a = Hose()
    print(a.market_index('2020-11-02','2021-11-02'))
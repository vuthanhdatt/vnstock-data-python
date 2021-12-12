import vnstock_data.data.price as price
import vnstock_data.data.ticket as ticket
from vnstock_data.base import BaseStock

class UpCom(BaseStock):
    def __init__(self, cookies) -> None:
        super().__init__()
        self.__cookies = cookies
        self.exchange = 'upcom'

    def market_index(self, start, end):
        '''
        Return UpCom market index from starting date to ending date.
        Data contain information about `PreClose`, `Open`, `Close`, `High`, `Low`, `Change(%)`, `Volume`, `MarketCap`
        
        Paramaters
        ----------
        start: string(MM-DD-YYYY), starting date
        end: string(MM-DD-YYYY), ending date
        
        Return
        ------
        DataFrame

        Note
        ----

        Because of limitation from Vietstock, free user only approach to data within 1 years. 
        Currently, I don't figure out how to beyond this limit. In the future, I'll try to solve this 
        problem and update as soon as I can.

        I also update for more various input type in future. In this version, it's only support string.

        Example
        -------
        >>> upcom = Hose(user_cookies)
        >>> upcom.market_index('02-05-2021','11-05-2021')
        >>>             PreClose    Open   Close    High     Low Change(%)     Volume     MarketCap
            Date
            2021-11-05    107.38  107.38  108.20  108.24  106.58      0.76  176304069  1.432800e+09
            2021-11-04    106.98  106.98  107.38  107.41  106.27      0.38  105892732  1.424375e+09
            2021-11-03    106.93  106.93  106.98  108.01  106.25      0.04  170081688  1.418124e+09
            2021-11-02    105.95  105.95  106.93  106.96  105.38      0.92  147567306  1.433885e+09
            2021-11-01    105.38  105.38  105.95  106.25  105.14      0.54  135917521  1.422570e+09
            ...              ...     ...     ...     ...     ...       ...        ...           ...
            2021-02-18     75.74   75.74   75.35   76.35   75.19     -0.52   57829290  1.014449e+09
            2021-02-17     73.81   73.82   75.74   75.81   73.82      2.61   46938986  1.005442e+09
            2021-02-09     72.65   72.66   73.81   73.81   72.55       1.6   33218517  9.864389e+08
            2021-02-08     73.89   73.89   72.65   73.98   72.41     -1.68   48761377  9.748888e+08
            2021-02-05     74.06   74.07   73.89   74.48   73.43     -0.24   80604156  9.892322e+08
        '''
        return price.get_market_index_history(self.exchange,start, end,cookies=self.__cookies)

     
    def all_company_info(self, industry_type='all', bussines_type='all', basic=True):
        '''
        Return all companies in UpCom exchange, users can choose industry type either business type. Users 
        can also choose basic return or not. If `basic=True` return only company code and exchange 
        where their listing. If `basic=False` return `Code`,`Name`,`IndustryName`,`TotalShares`

        Paramaters
        ----------
        industry_type: string, industry id in :func:`~main.VnStock.industry_type`
        b_type: string, business code in :func:`~main.VnStock.business_type`
        basic: boolen

        Return
        ------
        DataFrame
        
        '''
        com_info = ticket.get_all_com(self.exchange, self.__cookies, industry=industry_type, b_type=bussines_type,basic=basic)
        com_info.drop('Exchange',axis=1,inplace=True)
        return com_info
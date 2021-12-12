import vnstock_data.data.price as price
import vnstock_data.data.ticket as ticket
from base import BaseStock

class Hnx(BaseStock):
    def __init__(self, cookies) -> None:
        super().__init__()
        self.__cookies = cookies
        self.exchange = 'hnx'

    def market_index(self, start, end):
        '''
        Return HNX market index from starting date to ending date.
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
        >>> hnx = Hnx(user_cookies)
        >>> hnx.market_index('02-05-2021','11-05-2021')
        >>>             PreClose    Open   Close    High     Low Change(%)     Volume    MarketCap
            Date
            2021-11-05    422.42  422.42  427.64  428.52  422.36      1.24  146633246  461317662.0
            2021-11-04    415.71  415.71  422.42  422.92  413.84      1.62  140218109  456206974.0
            2021-11-03    424.11  424.11  415.71  430.31  415.70     -1.98  221120640  449023297.0
            2021-11-02    415.54  415.54  424.11  424.83  415.54      2.06  188401546  458843039.0
            2021-11-01    412.12  412.12  415.54  420.42  412.12      0.83  172918691  450053428.0
            ...              ...     ...     ...     ...     ...       ...        ...          ...
            2021-02-18    230.02  230.57  230.96  232.24  229.96      0.17  127256363  259495700.0
            2021-02-17    224.90  225.45  230.02  230.43  224.04      2.28   83583027  260028704.0
            2021-02-09    220.76  220.76  224.90  225.36  220.23      1.87   76920423  253030068.0
            2021-02-08    223.84  223.84  220.76  227.32  219.09     -1.38  125753227  248376384.0
            2021-02-05    223.68  223.68  223.84  227.19  221.88      0.07  109608645  251106922.0


        '''
        return price.get_market_index_history(self.exchange,start, end,cookies=self.__cookies)

    def all_company_info(self, industry_type='all', bussines_type='all', basic=True):
        '''
        Return all companies in HNX exchange, users can choose industry type either business type. Users 
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
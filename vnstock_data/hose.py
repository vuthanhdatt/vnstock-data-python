import vnstock_data.data.price as price
import vnstock_data.data.ticket as ticket
from base import BaseStock


class Hose(BaseStock):
    def __init__(self, cookies) -> None:
        super().__init__()
        self.__cookies = cookies
        self.exchange = 'hose'

    def market_index(self, start, end):

        '''
        Return HOSE market index from starting date to ending date.
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
        >>> hose = Hose(user_cookies)
        >>> hose.market_index('02-05-2021','11-05-2021')
        >>>             PreClose     Open    Close     High      Low Change(%)      Volume     MarketCap
            Date
            2021-11-05   1448.34  1450.71  1456.51  1459.49  1444.51      0.56   874070856  5.648438e+09
            2021-11-04   1444.30  1442.89  1448.34  1451.98  1435.84      0.28   929526879  5.616765e+09
            2021-11-03   1452.46  1460.44  1444.30  1463.63  1444.30     -0.56  1505103001  5.597664e+09
            2021-11-02   1438.97  1439.61  1452.46  1452.46  1438.83      0.94  1009457944  5.625759e+09
            2021-11-01   1444.27  1449.32  1438.97  1451.81  1435.57     -0.37  1132355594  5.573175e+09
            ...              ...      ...      ...      ...      ...       ...         ...           ...
            2021-02-18   1155.78  1157.10  1174.38  1174.38  1148.66      1.61   614819219  4.424568e+09
            2021-02-17   1114.93  1127.46  1155.78  1151.54  1127.46      3.66   507695043  4.355273e+09
            2021-02-09   1083.18  1090.88  1114.93  1114.93  1078.98      2.93   519814193  4.201332e+09
            2021-02-08   1126.91  1127.06  1083.18  1127.06  1075.10     -3.88   696599614  4.078789e+09
            2021-02-05   1112.19  1114.79  1126.91  1126.91  1112.19      1.32   529870404  4.243698e+09

        '''
        return price.get_market_index_history(self.exchange,start, end,cookies=self.__cookies)
    
    def all_company_info(self, industry_type='all', bussines_type='all', basic=True):
        '''
        Return all companies in HOSE exchange, users can choose industry type either business type. Users 
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


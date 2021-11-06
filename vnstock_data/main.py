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
        return ticket.get_bussiness_type(self.__cookies)

    @property
    def industry_type(self):
        return ticket.get_industry_list(self.__cookies)

    def all_company_info(self, industry_type='all', bussines_type='all', basic=True):
        return  ticket.get_all_com(self.exchange, self.__cookies, industry=industry_type, b_type=bussines_type,basic=basic)
    
    def price(self, symbol, start, end):
        '''
        Return price data of choosen company from starting date to ending date.
        Data include `High`, `Low`, `Open`, `Close`, `Volume`, `Adj Close`, `Average`, `High-Low`
        In future update, I will support taking multi companies.

        Paramaters
        ----------
        symbol: string, company stock code, etc. HPG, FTS...
        start: string(MM-DD-YYYY), starting date
        end: string(MM-DD-YYYY), ending date

        Return
        ------
        DataFrame

        Example
        ------
        >>> vndata = VnStock(user_cookies)
        >>> vndata.price('FTS', '02-05-2021','11-05-2021')
        >>>              High    Low   Open  Close   Volume  Adj Close  Average  High-Low
            Date
            2021-11-05  74000  69500  73500  71200   941700      71200    71833      4500
            2021-11-04  75000  70500  70500  73300   955800      73300    72710      4500
            2021-11-03  72000  68300  68300  70500  1334000      70500    70361      3700
            2021-11-02  68500  66600  67000  68000  1293500      68000    67503      1900
            2021-11-01  66300  62000  62700  66300  1389900      66300    64771      4300
            ...           ...    ...    ...    ...      ...        ...      ...       ...
            2021-02-18  17200  16650  16900  16800   533700      15000    16912       550
            2021-02-17  16800  16150  16400  16800   563900      15000    16444       650
            2021-02-09  16100  15500  15700  15900   382000      14200    15830       600
            2021-02-08  16500  15400  16400  15700   590500      14000    16088      1100
            2021-02-05  16500  16000  16150  16350   258000      14600    16248       500

        '''
        return price.get_price_history(symbol,start,end,self.__cookies)



    
    

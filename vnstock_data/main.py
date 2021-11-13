import data.price as price
import data.ticket as ticket
import data.financeinfo as fi
from base import BaseStock

class VnStock(BaseStock):
    def __init__(self, cookies:dict) -> None:
        super().__init__()
        self.__cookies = cookies
        self.exchange = 'all'
    
    @property
    def business_type(self):
        '''
        Return companies type in market
        
        Return
        ------
        DataFrame

        Example
        -------
        >>> vndata = VnStock(user_cookies)
        >>> vndata.business_type
        >>>                               Name
            Code
            JSC            Joint Stock Company
            IC               Insurance Company
            SC                Security Company
            B                             Bank
            FC                Fund Certificate
            OFI   Other Financial Institutions
            FMC        Fund Management Company
            AC                Auditing Company

        '''
        result =  ticket.get_business_type(self.__cookies)
        result.set_index('Code', inplace=True)
        return result

    @property
    def industry_type(self):
        '''
        Return industry type in market
        
        Return
        ------
        DataFrame

        Example
        -------
        >>> vndata = VnStock(user_cookies)
        >>> vndata.industry_type
        >>>                                                    Name
            ID
            100                              Agriculture Production
            200       Mining, Quarrying, and Oil and Gas Extraction
            300                                           Utilities
            400                        Construction and Real Estate
            600                                     Wholesale Trade
            800                      Transportation and Warehousing
            900                          Information and Technology
            1000                              Finance and Insurance
            1100                                 Rental and Leasing
            1200   Professional, Scientific, and Technical Services
            1300            Management of Companies and Enterprises
            1400  Administrative and Support and Waste Managemen...
            1500                               Educational Services
            1600                  Health Care and Social Assistance
            1700                Arts, Entertainment, and Recreation
            2000                              Public Administration
            1900      Other Services (except Public Administration)
            700                                        Retail Trade

        '''
        return ticket.get_industry_list(self.__cookies)

    def all_company_info(self, industry_type='all', business_type='all', basic=True):
        '''
        Return all companies, users can choose industry type either business type. Users can also
        basic return or not. If `basic=True` return only company code and exchange where their listing. 
        If `basic=False` return `Code`,`Name`,`IndustryName`,`TotalShares`,`Exchange`

        Paramaters
        ----------
        industry_type: string, industry id in :func:`~main.VnStock.industry_type`
        b_type: string, business code in :func:`~main.VnStock.business_type`
        basic: boolen

        Return
        ------
        DataFrame
        
        '''
        return  ticket.get_all_com(self.exchange, self.__cookies, industry=industry_type, b_type=business_type,basic=basic)
    
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
    
    def update_finance_result(self, industry='all'):
        '''
        Return up to date finance result of current quarter.

        Note that the result depend on Vietstock update progess, so may be the result don't has companies
        that have announced their finance result on current quarter.

        Paramaters
        ----------
        industry: string, industry type. See more at :func:`~main.VnStock.industry_type`

        Example
        -------
        >>> vndata = VnStock(user_cookies)
        >>> vndata.update_finance_result('100')
        >>>    Symbol   NetProfit  Profit_DiffPreviousTerm(%)  Profit_DiffSameTerm(%)  ...    P/E   BVPS   NetRevenue  Exchange
            0     HSL    1.316188                        32.3                   329.2  ...   10.5  14729    52.026634      HOSE
            1     HNG   -0.181341                         0.0                     0.0  ...   42.9      6     0.379913      HOSE
            2     CTP    0.012626                       -97.9                   -99.2  ...  154.7  12383    11.672374       HNX
            3     SJF    9.200734                       475.3                     0.0  ...   96.4  10545    40.168729      HOSE
            4     VIF    8.231164                       -89.0                   -87.5  ...   24.9  13661   410.253070       HNX
            5     ASM  260.859532                       203.0                   165.0  ...    9.2  28573  2415.393121      HOSE
            6     HAG   23.707239                       -72.5                     0.0  ...   -6.3   5352   554.141153      HOSE
            7     NSC   33.478289                       -46.8                    10.0  ...    7.2  69375   405.274789      HOSE
            8     HKT   -0.249398                         0.0                     0.0  ...  -14.9  10963    12.167036       HNX
            9     APC   -6.306495                         0.0                     0.0  ...   76.5  32127    26.565051      HOSE
            10    PSW   23.377377                        93.8                 10378.5  ...   11.2  13045   565.896915       HNX
            11    SSC    8.384454                       -49.7                   -42.0  ...   16.5  26177    60.051648      HOSE

        '''
        return fi.update_finance_result(self.__cookies, industry)



    
    

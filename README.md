# Vietnam Stock Data Python package

___

## 1. Introduction
Inspire from [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/) package. I want to create a package that can handle with Vietnam data. And not only trading data, I also want to access to other finance info like balance sheet or finance ratios. With that purpose, I've created this package to handle all that things. Currently this package is still in progress, in the future I will update more helpful function.

## 2. Installation
`pip install git+https://github.com/vuthanhdatt/vnstock-data-python.git`

## 3. Usage

User need to obtain Vietstock cookies to access data from their website. See more at [docs](https://vnstock-data-python.readthedocs.io/en/latest/#usage).

## 4. Example
Get OHLCV data of `FTS` from `05-02-2021` to `05-11-2021` 
```py
from vnstock_data.all_exchange import VnStock

COOKIES={"vts_usr_lg":"ABCDEF","language": "en-US","__RequestVerificationToken":"GhijKL"}

vndata = VnStock(COOKIES)

vndata.price('FTS', '02-05-2021','11-05-2021')
>>>                 High    Low   Open  Close   Volume  Adj Close  Average  High-Low
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
```
For more information, visit [API Reference](https://vnstock-data-python.readthedocs.io/en/latest/api/).
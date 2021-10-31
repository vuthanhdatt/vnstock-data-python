from ticket import company_ticket
from data import price_data

class StockData(object):
    def __init__(self, cookies:dict) -> None:
        super().__init__()
        self._cookies = cookies

    def get_company_ticket(self):
        return company_ticket()
    def get_company_price(self, ticket):
        return price_data(ticket, self._cookies)


if __name__ == '__main__':
    a = StockData({'PHPSESSID' : 'ioiccg4dffdsu46d58h4pepjk4'})
    print(a.get_company_price('HPG'))

    
    

import requests
import json

class Markit:
    def __init__(self):
        self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
        self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json"
    def company_search(self,company):
        url = self.lookup_url+'?input='+company.upper()
        r = requests.get(url,timeout=2)
        if r.status_code==200:
            company_list = json.loads(r.text)
            if company_list!=[]:
                symbol = company_list[0]['Symbol']
                print("company symbol :",symbol)
                return symbol
            
    def get_quote(self,company):
        q_url = self.quote_url+'?symbol='+company.upper()
        r = requests.get(q_url,timeout=2)
        if r.status_code==200:
            stockInfo = json.loads(r.text)
            company_name=stockInfo['Name']
            company_stock_price = stockInfo['LastPrice']
            print("company name ::",company_name)
            print("LastPrice::",company_stock_price)

    		
def Getcompany(stockName):
    company= Markit()
    return company.company_search(stockName)
def GetCurrentPrice(stockSymbol):
    company = Markit()
    return company.get_quote(stockSymbol)


	


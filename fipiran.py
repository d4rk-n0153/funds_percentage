from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import regs
import pandas as pd
from json import loads

class fipiran(scrapy.Spider):
    fund_name=[]
    deposit=[]
    five_best=[]
    stock=[]
    bond=[]
    other=[]
    cash=[]
    name="blahblah"
    start_urls=['https://fund.fipiran.ir/api/v1/fund/getfund?regno=11777']
    for _ in regs.regs:
        start_urls.append(regs.url+f"{_}")
        
    def parse(self, response):
        self.deposit.append((loads(response.text).get('item')).get('deposit'))
        self.fund_name.append((loads(response.text).get('item')).get('name'))
        self.five_best.append((loads(response.text).get('item')).get('fiveBest'))
        self.stock.append((loads(response.text).get('item')).get('stock'))
        self.bond.append((loads(response.text).get('item')).get('bond'))
        self.other.append((loads(response.text).get('item')).get('other'))
        self.cash.append((loads(response.text).get('item')).get('cash'))
        df=pd.DataFrame({
            'name': self.fund_name,
            'stock': self.stock,
            'deposit': self.deposit,
            # 'five_best': self.five_best,
            'bond': self.bond,
            'other': self.other,
            'cash': self.cash,
            
        })
        
        df.to_excel('fipiran.xlsx')

runner = CrawlerRunner()
d = runner.crawl(MySpider)
d.addBoth(lambda _: reactor.stop())







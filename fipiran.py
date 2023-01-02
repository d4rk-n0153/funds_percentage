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
    name="fipiran"
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
        df=({
            'name': self.fund_name,
            'stock': self.stock,
            'deposit': self.deposit,
            'bond': self.bond,
            'other': self.other,
            'cash': self.cash,
            
        })
        return df
        # df.to_html('templates/funds.html')

runner = CrawlerRunner()
d = runner.crawl(fipiran)
d.addBoth(lambda _: reactor.stop())







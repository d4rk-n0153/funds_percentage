from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess
import regs
import pandas as pd
from json import loads

class fipiran(scrapy.Spider):
    # custom_settings={
    #     'FEEDS':{'static/DB/DB.json':{'format': 'json',
    #         'encoding': 'utf8',
    #             'store_empty': False, 'fields': None, 'indent': 4,}}}
    name="fipiran"
    start_urls=[regs.url+f"{_}" for _ in regs.regs]   
    def parse(self, response):
        df={
            'name': ((loads(response.text).get('item')).get('name')),
            'stock': (loads(response.text).get('item')).get('stock'),
            'deposit': (loads(response.text).get('item')).get('deposit'),
            # 'five_best': self.five_best,
            'bond':((loads(response.text).get('item')).get('bond')),
            'other':((loads(response.text).get('item')).get('other')),
            'cash': ((loads(response.text).get('item')).get('cash')),
         }
        
        with open("static/DB/DB.json", "wb",encoding="utf-8") as file:
            file.write(str(df))

runner = CrawlerRunner()
d = runner.crawl(fipiran)
d.addBoth(lambda _: reactor.stop())

# runner=CrawlerProcess()
# runner.crawl(fipiran)
# runner.start()





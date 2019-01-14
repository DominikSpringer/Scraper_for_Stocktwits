from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.conf import settings
from scrapy import http
import re
import json
import time
import logging
import sys
try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

from datetime import datetime

sys.path.insert(0, 'C:/Temp/twitter/StocktwitsScraper')
from StocktwitsScraper.items import Twit

logger = logging.getLogger(__name__)


class StocktwitsScraper(CrawlSpider):
    name = 'twitscraper'
    allowed_domains = ['stocktwits.com']

    def __init__(self, query='', lang=''):

        self.query = query
        self.url = "https://api.stocktwits.com/api/2/streams/symbol/%s.json?max=%s&filter=top"
        self.url_start = "https://api.stocktwits.com/api/2/streams/symbol/%s.json?filter=top" 


    def start_requests(self):
        url = self.url_start % quote(self.query)
        yield http.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        data = json.loads(response.body.decode("utf-8"))
        max_position = data['cursor']['max']
        
        for twit_n in data['messages']:
            twit=Twit()
            twit['body']=twit_n['body']
            twit['twit_id']=twit_n['id']
            twit['created_at']=twit_n['created_at']
            twit['sentiment']=twit_n['entities']['sentiment']
            yield twit

        # get next page
        url = self.url % (quote(self.query), max_position)
        yield http.Request(url, callback=self.parse_page)


# comment the follwoing lines in case you want to run the crawler from the command line
# for further details please check the readme file attached to this code
process = CrawlerProcess(settings)
process.crawl('twitscraper', query='APPL')
process.start(stop_after_crawl=True) # the script will block here until the crawling is finished
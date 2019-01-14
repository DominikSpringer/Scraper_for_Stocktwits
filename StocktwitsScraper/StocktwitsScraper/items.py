from scrapy import Item, Field


class Twit(Item):
    twit_id = Field()    # tweet id
    body = Field()       # tweet url
    created_at = Field() # post time
    sentiment = Field()  # sentiment of stocktwits
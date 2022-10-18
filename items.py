# items.py
from scrapy import Item, Field


class QuoteItem(Item):
     title=Field()
     img=Field()
     content=Field()
     dateup=Field()
     url=Field()
     
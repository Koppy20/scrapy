# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class BaoqbPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='baoQB'
    )
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        return item
    def process_item(self, item, spider):
        self.cur.execute(""" insert into baoqb1 (title, img, content, dateup, url) values (%s,%s,%s,%s,%s)""", (
            item["dateup"],
            str(item["title"]),
            str(item["img"]),
            item["content"]
        ))
        self.conn.commit()
        return item

    
    def close_spider(self, spider):

        
        self.cur.close()
        self.conn.close()









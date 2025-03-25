# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter

# Scraped data -> Item containers -> json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mango database

import sqlite3

class QuotetutorialPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_db""")
        self.curr.execute("""
            CREATE TABLE IF NOT EXISTS quotes_tb (
                title TEXT,
                author TEXT,
                tags TEXT
            )
        """)

    def process_item(self, item, spider):
        self.store_tb(item)
        return item

    def store_tb(self,item):
        self.curr.execute("""insert into quotes_tb values (?,?,?)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))

        self.conn.commit()

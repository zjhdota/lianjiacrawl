# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import hashlib
from bson.objectid import ObjectId

class LianjiaPipeline(object):
    def __init__(self,):
        self.con = pymongo.MongoClient(host="127.0.0.1",port=27017)
        db = self.con['lianjia']
        self.collection = db['rent']

    def process_item(self, item, spider):
        md5 = hashlib.md5()
        md5.update(item['url'].encode('utf-8'))
        date = {
            '_id': md5.hexdigest(),
            'name':item['name'],
            'title':item['title'],
            'pattern':item['pattern'],
            'direction':item['direction'],
            'url':item['url'],
            'location':item['location'],
            'year':item['year'],
        }
        if not self.collection.find_one({'_id':date['_id']}):
            self.collection.insert(date)
        return item

    def close_item(self, spider):
        self.con.close()

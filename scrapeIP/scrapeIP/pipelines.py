# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
from scrapeIP import items

class ScrapeipPipeline(object):
	def process_item(self, item, spider):
		client = pymongo.MongoClient(host='127.0.0.1', port=12345)
		db = client['ip']
		coll = db['sheet']
		if coll.find({'ip':item['ip']}).count() <= 1:
			coll.insert_one(item)

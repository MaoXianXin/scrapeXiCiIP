import pymongo

client = pymongo.MongoClient(host='127.0.0.1',port=12345)
db = client['ip']
coll = db['sheet']

if coll.find({'ip':'15.48.48.48:8080'}).count() == 0:
	print(coll.find({'ip':'15.48.48.48:8080'}).count())
	print(type(coll.find({'ip':'15.48.48.48:8080'}).count()))
	coll.insert_one({'ip':'15.48.48.48:8080'})

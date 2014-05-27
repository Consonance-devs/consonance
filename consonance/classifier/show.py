
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 3001)
db = client.meteor
music = db.Consonance

for m in music.find():
	print "Name: " + m["music"]
	print "First 10 Peaks: "
	print m["peaks"][0:10]
	print "Lyrics: " + m["lyrics"]
	print



from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Consonance
music = db.music

for m in music.find():
	print "Name: " + m["music"]
	print "First 10 Peaks: "
	print m["peaks"][0:10]
	print "Lyrics: " + m["lyrics"]
	print


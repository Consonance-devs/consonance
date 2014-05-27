
INDEX = 0
HEADER = 1
TEXT = 2

from pymongo import MongoClient
client = MongoClient('127.0.0.1', 3001)
db = client.meteor
lyrics = db.Lyrics

def parsems(s):
	return int(s[0:2])*1000*60*60 + int(s[3:5])*1000*60 + int(s[6:8])*1000 + int(s[9:12])

def readlyrics(filepath, userid):
	print userid

	state = INDEX
	index = 0
	time = 0
	text = ""
	result = []
	#print "filepath: " + filepath
	#f = open(filepath, 'r')
	f = open(filepath, 'r')
	print "/home/michel/data/db/Kings Of Leon - Use Somebody.srt" == filepath
	print "<" + "/home/michel/data/db/Kings Of Leon - Use Somebody.srt" + ">"
	print "<" + filepath + ">"
	while True:
		if state == INDEX:
			line = f.readline()
			if line == '':
				break
			else:
				d = line.split()[0]
				#index = int(d)
				index+=1
		elif state == HEADER:
			line = f.readline()
			raw = line.split()
			time = parsems(raw[2]) - parsems(raw[0])
		elif state == TEXT:
			text = ""
			while True:
				line  = f.readline()
				if line == "\n" or line == "":
					break
				text += line
			result.append((index, time, text))
			#print index, time, text

		state = (state + 1) % 3

		if line == "":
			break

	lyrics.remove({"userid": userid})
	print "userid: " + userid
	for i in result:
		lyrics.insert({"index": i[0], "time": i[1], "text": i[2], "userid": userid})

		#print "<" + line + ">"
		
#readlyrics("/home/michel/data/db/Aerosmith - I Dont Want To Miss A Thing.srt", )

#readlyrics("/home/michel/data/db/Kings Of Leon - Use Somebody.srt", "asd")
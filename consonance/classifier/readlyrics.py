
INDEX = 0
HEADER = 1
TEXT = 2

from pymongo import MongoClient
client = MongoClient('127.0.0.1', 3001)
db = client.meteor
lyrics = db.Lyrics

def parsems(s):
	return int(s[0:2])*1000*60*60 + int(s[3:5])*1000*60 + int(s[6:8])*1000 + int(s[9:12])

def getText(s):
	return '<br>'.join(s.split('\n'))

def readlyrics(filepath, userId):
	print userId

	state = INDEX
	index = 0
	time = 0
	start = 0
	end = -1
	text = ""
	result = []
	
	f = open(filepath, 'r')
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
			start = parsems(raw[0])
			time = parsems(raw[2]) - start
		elif state == TEXT:
			text = ""
			while True:
				line  = f.readline()
				if line == "\n" or line == "":
					break
				text += line

			if len(result) > 0:
				t = result[len(result)-1][2] + result[len(result)-1][1];
				result.append((index, start - t, t, ""));
				index += 1;
			result.append((index, time, start, getText(text) ))
			#print index, time, text

		state = (state + 1) % 3

		if line == "":
			break

	lyrics.remove({"userId": userId})
	print "userId: " + userId
	for i in result:
		lyrics.insert({"index": i[0], "time": i[1], "start": i[2], "text": i[3], "userId": userId})

	print "Added Lyrics to Lyrics Collection."

	
		
#readlyrics("/home/michel/data/db/Aerosmith - I Dont Want To Miss A Thing.srt", )

from fingerprint import findpeaks
from sys import argv
from os import system
from compare2 import loadmusic

from pymongo import MongoClient
client = MongoClient('127.0.0.1', 3001)
db = client.meteor
music = db.Consonance

def main():
	
	if len(argv) >= 3:
		#print len(argv)
		peaks, duration = loadmusic(argv[1])

		d = {"music": argv[1], "peaks": peaks}
		cmd = "cp \"" + argv[2] + "\" ~/data/db/\"" + argv[1].split('.')[0] + ".srt\""
		#print cmd
		system(cmd)
		d["lyrics"] = argv[2]
		d["duration"] = duration

		if len(argv) > 3:
			d["author"] = argv[3]
		if len(argv) > 4:
			d["album"] = argv[4]

		#print d
		music.insert(d)
		print "Added " + d["music"] + " to music collection, with lyrics file " + "\"~/data/db/\"" + argv[1].split('.')[0] + ".srt\"" + "."
	else:
		print 'Usage: python2 insert.py musicfile.mp3 lyrics.srt [author] [album]'

main()

from fingerprint import findpeaks
from sys import argv
from os import system

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Consonance
music = db.music


def main():
	
	if len(argv) >= 3:
		print len(argv)
		peaks = []
		findpeaks(argv[1], peaks)
		peaks = sorted(peaks[0] + peaks[1])
		d = {"music": argv[1], "peaks": peaks}
		system("cp " + argv[2] + "data/" + argv[1] + ".srt")
		d["lyrics"] = argv[2]

		if len(argv) > 3:
			d["author"] = argv[3]
		if len(argv) > 4:
			d["album"] = argv[4]

		print d
		music.insert(d);

	else:
		print 'Usage: python2 insert.py musicfile.mp3 lyrics.srt [author] [album]'
	

main()

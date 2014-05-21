from fingerprint import findpeaks
from sys import argv

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Consonance
musictable = db.music


def main():
	if len(argv) > 1:
		print len(argv)
		music = []
		findpeaks(argv[1], music)
		music = sorted(music[0] + music[1])
		d = {"music": argv[1], "peaks": music}

		if len(argv) > 2:
			d["author"] = argv[2]
		if len(argv) > 3:
			d["album"] = argv[3]

		print d

	else:
		print 'Usage: python2 insert.py musicfile.mp3 [author] [album]'

main()

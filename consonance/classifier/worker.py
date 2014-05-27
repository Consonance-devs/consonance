
from fingerprint import findpeaks
from sys import argv
from os import system
from compare2 import *
from matplotlib import pyplot as plt
from readlyrics import *

from pymongo import MongoClient
client = MongoClient('127.0.0.1', 3001)
db = client.meteor
music = db.Consonance

#for i in music.find():
#	print i["music"]


# worker.py music.mp3

def main():
	best=0
	bestmatch = ""


	sample = loadmusic(argv[1])
	#print sample

	'''plt.title("Sample Peaks")
	plt.plot(*zip(*sample))
	plt.show()'''
	d = {}
	for m in music.find():
		k, s = compare(sample, m["peaks"]);
		d[k] = s
		if k > best:
			best = k
			bestmatch = m["music"]

	print correlation(d[max(d)], True)
	print bestmatch

	srtfile = "/home/michel/data/db/" + bestmatch.split('.')[0] + ".srt"
	print "srtfile: " + srtfile
	readlyrics(srtfile, argv[2])


main()

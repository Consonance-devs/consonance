
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
	best=10000000
	bestmatch = ""


	sample, sampleDuration = loadmusic(argv[1])
	#print sample

	'''plt.title("Sample Peaks")
	plt.plot(*zip(*sample))
	plt.show()'''
	d = {}
	for m in music.find():
		k, s = compare(sample, m["peaks"]);
		
		
		l = [abs(i-j) for i,j in s.items()]

		std = numpy.std(l)
		print m["music"], k, numpy.std(l)
		d[std] = s

		if std < best:
			best = std
			bestmatch = m["music"]

	#for index, matches in d.items():
		
		

	c = correlation(d[min(d)], False)
	print "correlation: ", c
	print bestmatch

	srtfile = "/home/michel/data/db/" + bestmatch.split('.')[0] + ".srt"
	print "srtfile: " + srtfile
	readlyrics(srtfile, argv[2])


	bmatch = music.find_one({"music": bestmatch})

	maxpeak = max([i for i,j in bmatch["peaks"] ])
	print "maxpeak: ", maxpeak
	duration = bmatch["duration"] * 1000
	print "duration: ", duration
	x = (c * duration) / maxpeak + sampleDuration
	print "x"
	print x

	'''
		maxpeak --- duration
		peak    --- x

		maxpeak --- peak
		duration --- x
	'''

main()


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


	sample, sampleDuration = loadmusic(argv[1])
	#print sample

	'''plt.title("Sample Peaks")
	plt.plot(*zip(*sample))
	plt.show()'''
	d = {}
	names = {}
	for m in music.find():
		
		print m["music"]
		k, s = compare(sample, m["peaks"]);
		compare_std(s)
		
		#l = [abs(i-j) for i,j in s.items()]
		#std = numpy.std(l)
		
		d[k] = s
		names[k] = m["music"]

		if k > best:
			best = k
			bestmatch = m["music"]

	#for index, matches in d.items():
	
	print 'best:', bestmatch
	match = max(d.keys())


	if len(d) >= 2:
		l = sorted(d.keys()) 
		bestind = l[len(l)-1]
		sbestind = l[len(l)-2]
		if diff(bestind, sbestind) < 0.01:
			a = compare_std(d[bestind])
			b = compare_std(d[sbestind])
			if b < a:
				match = sbestind
				bestmatch = names[sbestind]
				print "new best match: ", names[sbestind]	


	c = correlation(d[match])
	print "correlation: ", c
	

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

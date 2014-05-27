
from fingerprint import findpeaks
from sys import argv
from os import system

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Consonance
music = db.music

from compare2 import compare

from matplotlib import pyplot as plt

# worker.py music.mp3

def main():
	bbest=1000000
	bpos=0
	best=0
	bestmatch = ""

	samplepeaks = []
	sample = []
	findpeaks(argv[1], sample)
	samplepeaks = sorted(sample[0] + sample[1])
	print samplepeaks

	'''plt.title("Samplepeaks")
	plt.plot(*zip(*samplepeaks))
	plt.show()'''

	for m in music.find():
		print m["music"]
		#print m["peaks"]
		'''plt.title("peaks")
		plt.plot(*zip(*m["peaks"]))
		plt.show()'''
		best, s = compare(samplepeaks, m["peaks"]);
		print best, s
		if best < bbest:
			bbest = best
			bpos = s
			bestmatch = m["music"]

	print bestmatch
	print bpos


main()

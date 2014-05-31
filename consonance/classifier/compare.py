from fingerprint import findpeaks
from matplotlib import pyplot as plt
import numpy

lim = 10

def merge(arr):
	d = {}
	for i,j in  arr:
		if i not in d:
			d[i] = set()
		d[i].add(j)
	return d

def intersect(a, b):
	s = set()
	for i in a:
		for t in range(i-lim, i+lim):
			if t in b:
				s.add(i)
				break

	return s


def maxl(d):
	k, v = (0,0)
	for i in d:
		if d[i] > v:
			k = i
			v = d[i]
	return k, v

def compare(a, b):
	a = merge(a)
	b = merge(b)
	bestinc = 0
	best = 0

	d = {}
	for i in a.keys(): # for each time instant
		key,value = maxl({k:len(a[i] & el) for k,el in b.items() if k >= i} ) # in the music we are comparing our sample, we find the time instant with more peaks in common
		best += value # we increment the best variable, that stores a value that will be used to get the best match

		if value > 1:
			d[i] = key # if this match is good enough, we consider it

	return best, d


def loadmusic(name):
	'''Reads and returns the music peaks, given filename.
	'''
	m = []
	duration = findpeaks(name, m)
	
	if len(m) == 2:
		return sorted(m[0] + m[1]), duration
	else:
		return sorted(m[0]), duration


def correlation(order, plot=False):
	'''Given the correspondency of time instants from the sample and the most similar music, 
	   we find the start time of the first relatively to the second.
	'''

	keys = sorted(list(order.keys()))
	values = [order[i] for i in keys]
	#for i,j in zip(keys, values):
		#print i,j

	if plot:
		plt.plot(keys, values)

	#a, b = numpy.polyfit(keys, values, 1)
	
	tl = [abs(i-j) for i,j in zip(keys, values)] # get differences between time instants that correspond
	b = sum(tl) / len(tl) # get the average difference
	a = 1

	l = [i*a + b for i in 0, max(keys) ]
	print a, b

	if plot:
		plt.plot([0, max(keys)], [b, a*max(keys) + b] )
		plt.show()

	return b


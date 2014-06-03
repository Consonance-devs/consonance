from fingerprint import findpeaks
from matplotlib import pyplot as plt
import numpy

lim = 3

def merge(arr):
	d = {}
	for i,j in arr:
		if i not in d:
			d[i] = set()
		d[i].add(j)
	return d

def intersect(a, b):
	#return a & b
	s = set()
	for i in a:
		for t in range(i-lim, i+lim):
			if t in b:
				s.add(i)
				break

	return s


def maxl(d):
	k, v = (0,0)
	for i in sorted(d.keys()):
		if d[i] > v:
			k = i
			v = d[i]
	return k, v

def loadmusic(name):
	m = []
	duration = findpeaks(name, m)
	#print m
	if len(m) == 2:
		return sorted(m[0] + m[1]), duration
	else:
		return sorted(m[0]), duration

def compare(a, b): # compares the sample with each music
	a = merge(a)
	b = merge(b)
	bestinc = 0
	sim1 = 0
	sim = 0

	order = []
	d = {}
	for i in a.keys():
		key,value = maxl({k:len(intersect(a[i], el) ) for k,el in b.items()} )	#
		#key,value = maxl({k:len(a[i] & el) for k,el in b.items()} )

		sim1 += value
		if value > 1:
			d[i] = key
			sim += value
			print i, key, value

	print sim, "(", sim1, ")"
	return sim*50 + sim1, d


def correlation(order, plot=False):
	keys = sorted(list(order.keys()))
	values = [order[i] for i in keys]
	for i,j in zip(keys, values):
		print i,j

	if plot:
		plt.plot(keys, values)

	#a, b = numpy.polyfit(keys, values, 1)
	#a, b, _, _, _ = linregress(keys, values)
	tl = [abs(i-j) for i,j in zip(keys, values)]
	b = sum(tl) / len(tl)
	a = 1

	l = [i*a + b for i in 0, max(keys) ]
	print a, b

	#print a, b
	#print max(order.keys())

	'''
	for i in nx:
		#key,value = maxl({k:len(intersect(a[i], el) ) for k,el in b.items()} )	#
		key,value = maxl({k:len(merge(sample)[i] & el) for k,el in merge(music).items() if k/2 <= i*a + b and k*2 >= i*a + b } )
		order[i] = key
	'''

	if plot:
		plt.plot([0, max(keys)], [b, a*max(keys) + b] )
		plt.show()

	return b


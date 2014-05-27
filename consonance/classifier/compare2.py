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

	order = []
	for i in a.keys():
		#key,value = maxl({k:len(intersect(a[i], el) ) for k,el in b.items()} )	#
		key,value = maxl({k:len(a[i] & el) for k,el in b.items() if k >= i} )
		order.append(key)
		best += value

	#print order

	'''for inc in range(0, max(b)-max(a)):
		cur = 0
		for k in a.keys():
			if k+inc in b.keys():
				cur += len(a[k] & b[k+inc])
				#cur += len( intersect(a[k], b[k+inc] ))

		if cur > best:
			best = cur
			bestinc = inc'''


	'''for k in a.keys():
		if k+bestinc in b.keys():
			#print a[k]
			#print b[k]
			print list( intersect(a[k], b[k+bestinc]) )'''

	d = {}
	for i,v in zip(a.keys(),order):
		d[i] = v


	return best, d


def loadmusic(name):
	m = []
	findpeaks(name, m)
	#print m
	if len(m) == 2:
		return sorted(m[0] + m[1])
	else:
		return sorted(m[0])
		

def correlation(order, plot=False):
	if plot:
		plt.plot(order.keys(), order.values())

	a, b = numpy.polyfit(order.keys(), order.values(), 1)

	l = [i*a + b for i in 0, max(order.keys()) ]

	nx = []
	ny = []

	for i in order:
		if order[i]/2 <= i*a + b and order[i]*2 >= i*a + b:
			nx.append(i)
			ny.append(order[i])

	a, b = numpy.polyfit(nx, ny, 1)
	#print a, b
	#print max(order.keys())

	'''for i in nx:
		#key,value = maxl({k:len(intersect(a[i], el) ) for k,el in b.items()} )	#
		key,value = maxl({k:len(merge(sample)[i] & el) for k,el in merge(music).items() if k/2 <= i*a + b and k*2 >= i*a + b } )
		order[i] = key'''

	if plot:
		plt.plot([0, max(order.keys())], [b, a*max(order.keys()) + b])
		plt.show()

	return b


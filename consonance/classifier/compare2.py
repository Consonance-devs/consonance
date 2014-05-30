from fingerprint import findpeaks
from matplotlib import pyplot as plt
import numpy

lim = 10

def merge(arr):
	d = {}
	for i,j in arr:
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
	for i in sorted(d.keys()):
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
	d = {}
	for i in a.keys():
		#key,value = maxl({k:len(intersect(a[i], el) ) for k,el in b.items()} )	#
		key,value = maxl({k:len(a[i] & el) for k,el in b.items()} )
		order.append(key)
		

		#if value > 1:
		d[i] = key
		best += value
		print i, key, value

	return best, d

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

	
	#for i,v in zip(a.keys(),order):


def loadmusic(name):
	m = []
	duration = findpeaks(name, m)
	#print m
	if len(m) == 2:
		return sorted(m[0] + m[1]), duration
	else:
		return sorted(m[0]), duration


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


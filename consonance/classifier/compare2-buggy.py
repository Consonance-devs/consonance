from fingerprint import findpeaks
from matplotlib import pyplot as plt
import numpy
from scipy.stats import linregress

lim = 10

def merge(arr):
	d = {}
	for i,j in  arr:
		if i not in d:
			d[i] = set()
		d[i].add(j)
	return d

def intersect(a, b):
	return a & b
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
	vals = []

	d = {}
	for i in a.keys():
		#key,value = maxl({k:len(intersect(a[i], el) ) for k,el in b.items()} )	#
		key,value = maxl({k:len(intersect(a[i], el) ) for k,el in b.items() if k >= i} )
		order.append(key)
		vals.append(value)
		best += value
		
		#if value > 1:
		d[i] = key
			#print i, key, value
			

	'''t = sorted(list(d.keys()))
	p = 1
	for i in range(min(t), max(t)):
		if i > t[p]:
			p+=1
		if i not in t:
			d[i] = float(d[t[p]] - d[t[p-1]]) / (t[p] - t[p-1]) * i + t[d[p]]

		print i, d[i]'''

	'''
	diff (p-1) and p ----- diff d[p-1] and d[p]
	diff 
	'''

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

	'''d = {}
	for i,v,sim in zip(a.keys(), order, vals):
		if sim >= 2:
			d[i] = v
	'''

	return best, d


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

	nx = []
	ny = []

	'''for i in order:
		if order[i]/2 <= i*a + b and order[i]*2 >= i*a + b:
			nx.append(i)
			ny.append(order[i])

	a, b = numpy.polyfit(nx, ny, 1)'''
	print a, b

	#print a, b
	#print max(order.keys())

	'''for i in nx:
		#key,value = maxl({k:len(intersect(a[i], el) ) for k,el in b.items()} )	#
		key,value = maxl({k:len(merge(sample)[i] & el) for k,el in merge(music).items() if k/2 <= i*a + b and k*2 >= i*a + b } )
		order[i] = key'''



	if plot:
		plt.plot([0, max(keys)], [b, a*max(keys) + b] )
		plt.show()

	return b * 2048


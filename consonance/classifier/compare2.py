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

def diff(a, b):
	return abs(a-b)/max(a,b)

def compare(a, b): # compares the sample with each music
	a = merge(a)
	b = merge(b)
	bestinc = 0
	sim1 = 0
	sim = 0

	order = []
	d = {}
	for i in a.keys():
		key,value = maxl({k:len(intersect(a[i], el) ) for k,el in b.items()} )

		sim1 += value
		if value > 1:
			d[i] = key
			sim += value

	print sim, "(", sim1, ")"
	return sim*50 + sim1, d

def compare_std(order):
	keys = sorted(list(order.keys()))
	values = [order[i] for i in keys]

	tl = [abs(i-j) for i,j in zip(keys, values)]
	print '(len:', len(tl), ')',
	if len(tl) > 1:
		r = numpy.std(tl)/len(tl)
		print '(', r, ')'
		return r

	return -1

def next_ind(l, v):
	for i in range(len(l)):
		if v > l[i]:
			return i


def correlation(order, plot=False):
	tkeys = sorted(order.keys())
	for i in range(min(order.keys()), max(order.keys())):
		if i not in order:
			order[i] = order[i-1]+1
	
	keys = sorted(list(order.keys()))
	values = [order[i] for i in keys]

	if plot:
		plt.plot(keys, values)


	tl = [abs(i-j) for i,j in zip(keys, values)]
	#b = sum(tl) / len(tl)
	b = sorted(tl)[len(tl)/2]
	a = 1

	'''
	tl = [abs(i-j) for i,j in zip(keys, values) if abs(i-j) + i > b/2 and abs(i-j) + i < b*2]
	b = sum(tl) / len(tl)
	a = 1
	'''
	
	#l = [i*a + b for i in 0, max(keys) ]

	if plot:
		plt.plot([0, max(keys)], [b, a*max(keys) + b] )
		plt.show()


	return b

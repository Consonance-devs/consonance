
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
		key,value = maxl({k:len(a[i] & el) for k,el in b.items()} )
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

	return best, order



lim = 40

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

	return s


def compare(a, b):
	bestinc = 0
	best = 0

	for inc in range(0, max(b)):
		cur = 0
		for k in a.keys():
			if k+inc in b.keys():
				#cur += len(a[k] & b[k+inc])
				cur += len( intersect(a[k], b[k+inc] ))

		if cur > best:
			best = cur
			bestinc = inc


	for k in a.keys():
		if k+bestinc in b.keys():
			#print a[k]
			#print b[k]
			print list( intersect(a[k], b[k+bestinc]) )

	return best, bestinc


from fingerprint import findpeaks
from compare2 import *
from data import *
from matplotlib import pyplot as plt
import numpy

#music1 = loadmusic("music1.mp3")
#print music1
#music2 = loadmusic("music2.mp3")
#print music2
#music3 = loadmusic("music3.mp3")
#print music3

sample1 = loadmusic("sample1.mp3")
sample2 = loadmusic("sample2.mp3")
sample3 = loadmusic("sample3.mp3")
noise3 = loadmusic("/tmp/uJBp5bWNqNXXJFMMr.mp3")
print sample3
print noise3

print "sample1"
d = {}
k, v = compare(sample1, music1)
d[k] = v
k, v = compare(sample1, music2)
d[k] = v
k, v = compare(sample1, music3)
d[k] = v

correlation(d[max(d)], True)

print "sample2"
d = {}
k, v = compare(sample2, music1)
d[k] = v
k, v = compare(sample2, music2)
d[k] = v
k, v = compare(sample2, music3)
d[k] = v

correlation(d[max(d)], True)

print "sample3"
d = {}
k, v = compare(sample3, music1)
d[k] = v
k, v = compare(sample3, music2)
d[k] = v
d = {}
k, v = compare(sample3, music3)
d[k] = v

correlation(d[max(d)], True)

d = {}
k, v = compare(noise3, music3)
d[k] = v

correlation(d[max(d)], True)

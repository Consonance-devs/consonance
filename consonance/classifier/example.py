from fingerprint import findpeaks
from compare2 import compare

def loadmusic(name):
	m = []
	findpeaks(name, m)
	#print m
	return sorted(m[0] + m[1])
	

l = loadmusic("teste5.mp3")


music1 = loadmusic("music1.mp3")
music2 = loadmusic("music2.mp3")
music3 = loadmusic("music3.mp3")

sample1 = loadmusic("sample1.mp3")
sample2 = loadmusic("sample2.mp3")
sample3 = loadmusic("sample3.mp3")

compare(sample1, music1)
compare(sample1, music2)
compare(sample1, music3)

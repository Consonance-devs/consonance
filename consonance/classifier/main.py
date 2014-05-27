import os
import fingerprint
from fingerprint import findpeaks
import decoder

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Consonance
musictable = db.music

music1 = []
music2 = []
findpeaks("comeasyouare1.mp3", music1)
findpeaks("comeasyouare2.mp3", music2)

'''print "Sample1, Channel 1"
print music1[0]
print "Sample2, Channel 1"
print music2[0]
print "Sample1, Channel 2"
print music1[1]
print "Sample2, Channel 2"
print music2[1]'''

sample = music1
data = [music2]

music1 = sorted(music1[0] + music1[1])
music2 = sorted(music2[0] + music2[1])
print "Music1"
print music1
print "Music2"
print music2


dp = [[0 for col in range(len(music2))] for row in range(len(music1))]
s = 0

def val(music1, music2, i, j):
	if i>0 and j > 0:
		return min(dp[i][j-1]+20, dp[i-1][j]+20, dp[i-1][j-1] + abs(music1[i][1] - music2[j][1]))
	elif i==0 and j==0:
		return min(0, abs(music1[i][1] - music2[j][1]))
	elif i==0:
		return min(dp[i][j-1]+20, abs(music1[i][1] - music2[j][1]))
	else:
		return min(dp[i-1][j]+20, abs(music1[i][1] - music2[j][1]))

def match(music1, music2, i, j):
	global dp
	for i in range(len(music1)):
		for j in range(len(music2)):
			dp[i][j] = val(music1, music2, i, j)
			#print str(i) + ", " + str(j) + ": " + str(dp[i][j])

	print "dp"
	print dp[len(music1)-1]
	return min( (val, i) for (i, val) in enumerate(dp[len(music1)-1]) )
	

def reconstruct(i, j):
	if i>0 and j>0 and dp[i][j] == dp[i-1][j-1] + abs(music1[i][1] - music2[j][1]):
		reconstruct(i-1, j-1)
		print (i-1, j-1)
	elif i==0:
		print (i, j)
		global s
		s = j
	elif j!=0 and dp[i][j] == dp[i][j-1]+20:
		reconstruct(i, j-1)
		print (i, j-1)
	elif dp[i][j] == dp[i-1][j]+20:
		reconstruct(j-1, i)
		print (i-1, j)

best, index = match(music1, music2, 0, 0)
reconstruct(len(music1)-1, index)

print best, index
print s


dp = []
s = 0
music1 = []
music2 = []

P = 30

def val(music1, music2, i, j):
	global dp
	if i>0 and j > 0:
		return min(dp[i][j-1]+P, dp[i-1][j]+P, dp[i-1][j-1] + abs(music1[i][1] - music2[j][1]))
	elif i==0 and j==0:
		return min(0, abs(music1[i][1] - music2[j][1]))
	elif i==0:
		return min(dp[i][j-1]+P, abs(music1[i][1] - music2[j][1]))
	else:
		return min(dp[i-1][j]+P, abs(music1[i][1] - music2[j][1]))

def match(music1, music2, i, j):
	global dp
	for i in range(len(music1)):
		for j in range(len(music2)):
			dp[i][j] = val(music1, music2, i, j)
			#print str(i) + ", " + str(j) + ": " + str(dp[i][j])

	print "dp"
	print dp[len(music1)-1]
	return min( (val, i) for (i, val) in enumerate(dp[len(music1)-1]) )
	

def reconstruct(music1, music2, i, j):
	global dp
	if i>0 and j>0 and dp[i][j] == dp[i-1][j-1] + abs(music1[i][1] - music2[j][1]):
		print (i-1, j-1)
		reconstruct(music1, music2, i-1, j-1)
	elif i==0:
		print (i, j)
		global s
		s = j
	elif j!=0 and dp[i][j] == dp[i][j-1]+P:
		print (i, j-1)
		reconstruct(music1, music2, i, j-1)
	elif dp[i][j] == dp[i-1][j]+P:
		print (i-1, j)
		reconstruct(music1, music2, j-1, i)
		


def compare(music1, music2):
	global dp
	dp = [[0 for col in range(len(music2))] for row in range(len(music1))]

	print "match"
	best, index = match(music1, music2, 0, 0)
	print "reconstruct"
	reconstruct(music1, music2, len(music1)-1, index)
	print "end"

	print best, index
	print s

	print dp

	return (best, s)



from fingerprint import findpeaks
from compare2 import *

teste1 = []
teste2 = []
findpeaks("teste2.mp3", teste1)
findpeaks("teste2-1.mp3", teste2)

teste1 = sorted(teste1[0] + teste1[1])
teste2 = sorted(teste2[0] + teste2[1])

a = merge(teste1)
b = merge(teste2)
print a
print
print b

print compare(b, a)
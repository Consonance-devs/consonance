from database import *

def make_dic(arr):
    d = {}
    for time, freq in arr:
        if time not in d:
            d[time] = []
        d[time].append(freq)
    return d
    
def compare_point(at, atarget):
    i = 0
    for freq in at:
        if freq in atarget:
            i+=1
    return i
    
def compare(test, target):
    test_times = test.keys()
    target_times = target.keys()
    tries = []
    for i in range(len(target_times) - len(test_times)):
        s = 0
        for j in range(len(test_times)):
            s += compare_point(test[test_times[j]], target[target_times[i + j]])
        tries.append(s)
    return tries



print "Sample 1:"
print max(compare(make_dic(sample1), make_dic(music1)))
print max(compare(make_dic(sample1), make_dic(music2)))
print max(compare(make_dic(sample1), make_dic(music3)))

print "Sample 2:"
print max(compare(make_dic(sample2), make_dic(music1)))
print max(compare(make_dic(sample2), make_dic(music2)))
print max(compare(make_dic(sample2), make_dic(music3)))

print "Sample 3:"
print max(compare(make_dic(sample3), make_dic(music1)))
print max(compare(make_dic(sample3), make_dic(music2)))
print max(compare(make_dic(sample3), make_dic(music3)))
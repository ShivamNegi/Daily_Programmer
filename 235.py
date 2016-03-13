from math import sqrt

def factors(no):
	li = []
	for i in xrange(sqrt(no)):
		if no % i == 0:
			li.append(i)
	return li

num = int(raw_input())
li = factors(num)
print li
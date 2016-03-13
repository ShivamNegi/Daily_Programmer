#!usr/bin/env python 

import time
start_time = time.time()
#total_time = 0
n = 6
count = 0

for i in xrange(0,pow(10,n),7):
	'''if i% 7  == 0:
		k = int(str(i)[::-1])
		if k%7 == 0:
			count += 1'''

	if int(str(i)[::-1]) % 7 == 0:
		count += 1

	'''if(str(i)[0] == '1'):
		flag = 1
		for ch in str(i)[1:]:
			if ch != '0':
				flag = 0
				break

		if flag :
			print "\n\n--- %s seconds ---" %(time.time() -start_time)
			total_time += start_time
			print count
			count = 0
			start_time = time.time()'''

print count
print "\n\n--- %s seconds ---" %(time.time() -start_time)


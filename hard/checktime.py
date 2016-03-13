import time

i = pow(10,7)

flag = 1
start_time = time.time()
for ch in str(i)[1:]:
	if ch != '0':
		flag = 0
		break

if flag :
	print "is 10^*"
else:
	print "not."

print "\n\n--- %s seconds ---" %(time.time() -start_time)		
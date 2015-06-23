inp = []
n = input("Enter the number of inputs:")

month = {
    '01':'January',
    '02':'February',
    '03':'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':'July',
    '08':'August',
    '09':'September',
    '10':'October',
    '11':'November',
    '12':'December'
    }
#inputting data

for i in range(n):
        inp1 = raw_input()
        inp1 = inp1.split(' ')
        inp.append(inp1[0])
        inp.append(inp1[1])

for j in range(len(inp)):
    inp[j] = inp[j].split('-')

i = 0
out = []

for i in range(0,len(inp),2):
    print month[inp[i][1]],
    print inp[i][2],
    if inp[i][0] != inp[i+1][0] or  ( int(inp[i][0]) + 1 == int(inp[i+1][0]) and int(inp[i+1][1]) > int(inp[i][1]) ):
        print ',' + inp[i][0],
    print ' - ' + month[inp[i+1][1]],
    print inp[i+1][2],
    if inp[i+1][0] != '2015':
        print ',' + inp[i+1][0],
    print '\n'

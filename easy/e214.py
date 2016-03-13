import math

# inp = [int(x) for x in raw_input("Enter: ").split()]
inp = list(map(int, raw_input("Enter: ").split()))

avg = sum(inp) / len(inp)
variance = 0
for no in inp:
    variance += (no - avg) ** 2

variance /= len(inp)
print "variance: ", variance
std_dev = math.sqrt(variance)
print "Standard deviation", std_dev

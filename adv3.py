import math
from itertools import count

def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0,1,0),(0,0,-1),(1,-1,0),(1,0,1)]:
            for _ in range(s+ds):
                i += di; j += dj
                a[i,j] = sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                             for l in range(j-1,j+2))
                yield a[i,j]

def part2(n):
    for x in sum_spiral():
        if x>n: return x


def squareSize(num):
	i = 1
	while i**2 < num:
		i+=2
	return i

def layerOffset(ss):
	return int(math.floor(ss / 2))

def calcDistance(num):
	layer = squareSize(num)
	offset = layerOffset(layer)

	topBound = layer**2 - offset
	lowBound = topBound - (layer - 1)

	while abs(topBound - num) >= layer:
		topBound = lowBound
		lowBound = topBound - (layer - 1)

	print "topBound:", topBound
	print "lowBound:", lowBound
	print "offset:", offset
	if abs(topBound - num) > (num - lowBound):
		return (num - lowBound) + offset
	else:
		return abs(topBound - num) + offset

given = int(raw_input("Enter your number: "))
print(part2(given))


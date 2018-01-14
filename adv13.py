import sys
from collections import defaultdict

data = sys.stdin.readlines()
ranges = defaultdict(int)

for line in data:
	layer,_,depth = line.partition(": ")
	ranges[int(layer)] = int(depth)

amountOfLayers = max(ranges.keys())
skip = -1

while True:
	skip += 1
	total = 0

	for layer in range(0, amountOfLayers + 1):
		depth = ranges[layer]
		scannerMax = depth + depth - 2
		if scannerMax > 0:
			scanerPos = (layer + skip) % scannerMax
			if scanerPos > scannerMax:
				scanerPos = scannerPos - scannerMax
			if scanerPos == 0:
				total += 1 #layer * depth
		elif scannerMax == 0:
			total += 1 #layer * depth

	print skip
	if total == 0:
		print "Skip:",skip
		break

print total


from adv10 import knotHash

data = 'flqrgnkx'

used = 0

regions = []

for row in xrange(128):
	inp = knotHash(data+"-"+str(row))

	binary = bin(int(inp, 16))[2:]
	used += str(binary).count('1')

	col = 0
	for char in str(binary):
		if char == "1":
			regions.append([row, col])
		col += 1

print used

vis = set()

def search(x, y):
    if (0 <= min(x, y) <= max(x, y) < 128 and 
    	(x, y) not in vis and 
    	[x, y] in regions):
        vis.add((x, y))
        surroundingSquare = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
        for (x, y) in surroundingSquare:
            search(x, y)
        return True

print(sum(1 for x in range(0, 128) for y in range(0, 128) if search(x, y)))

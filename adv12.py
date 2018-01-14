import sys

data = sys.stdin.readlines()
graph = {}

for line in data:
	before,_,after = line.partition(" <-> ")
	after = after.strip().split(", ")
	
	before = int(before)
	after = map(lambda x: int(x), after)

	for token in after:
		if before not in graph:
			graph[before] = []
		if token not in graph:
			graph[token] = []
		graph[before].append(token)
		graph[token].append(before)


q = range(0, len(data) - 1)
groups = 0

while q:
	connectedToZero = [q[0]]
	vis = []

	while connectedToZero:
		a = connectedToZero.pop()
		for token in graph[a]:
			if token not in vis:
				vis.append(token)
				connectedToZero.append(token)

	q = [x for x in q if x not in vis]
	groups += 1

print groups
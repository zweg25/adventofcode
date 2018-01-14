import sys

def redistributer(arr, pos, total):
	if pos >= len(arr):
		pos = 0
	if total <= 0:
		return arr
	else:
		arr[pos] += 1
		return redistributer(arr, pos + 1, total - 1)


def listOfNumToStr(lis):
	return " ".join(str(x) for x in lis)

data = sys.stdin.readline()
data = data.split()
data = list(map(lambda elt: int(elt), data))

mem = []

i = 0

while listOfNumToStr(data) not in mem:
	mem.append(listOfNumToStr(data))
	index = data.index(max(data))
	total = data[index]
	data[index] = 0
	data = redistributer(data, index + 1, total)

lastSeen = mem.index(listOfNumToStr(data))
print(len(mem) - lastSeen)
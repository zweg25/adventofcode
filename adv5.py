import sys
data = sys.stdin.readlines()
data = list(map(lambda m: int(m), data))

sys.setrecursionlimit(1500)

def performJumps(arr, place, steps, stepsPlus):
	if place >= len(arr):
		return [steps]
	if steps == stepsPlus:
		return [steps, place]
	nextPlace = arr[place] + place
	if arr[place] >= 3:
		arr[place] -= 1
	else:
		arr[place] += 1
	steps += 1
	return performJumps(arr, nextPlace, steps, stepsPlus)

ret = [0, 0]
while len(ret) == 2:
	step = ret[0]
	p = ret[1]
	ret = performJumps(data, p, step, step+1000)

print ret[0]
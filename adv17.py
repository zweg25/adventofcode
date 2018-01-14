steps = 301
iterations = 2018


def spin(arr, pos, obj):
	pos = (pos + steps) % len(arr)
	arr.insert(pos, obj)

	pos += 1
	return arr, pos

currentPos = 0
arr = [0, 1]

for x in xrange(2, iterations):
	arr, currentPos = spin(arr, currentPos, x)


indexOf2017 = arr.index(2017)
print arr[indexOf2017 + 1]


# part 2
i = 0
for t in xrange(1,50000000+1):
    i = (i+steps) % t + 1
    if i == 1:
        val_after_0 = t
print val_after_0
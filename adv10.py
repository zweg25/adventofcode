import sys
import operator

def xor(str1, str2):
	return bool(str1) ^ bool(str2)

def int2hex(x):
	val = hex(x)[2:] # returns something like '0x15', so we remove the '0x'
	val = "0"+val if len(val)<2 else val # make sure 2 digits
	return val

def reverse_sublist(lst,start,end):
	i = 0
	length = end - start
	lstLength = len(lst)

	end -= 1

	while i < length / 2:
		endPos = (end - i) % lstLength
		startPos = (start + i) % lstLength

		tmp = lst[endPos]
		lst[endPos] = lst[startPos]
		lst[startPos] = tmp
		i += 1

		#print lst

	return lst

def knotHash(myInput):
	array = range(0, 256)
	arraySize = len(array)
	stepSize = 0
	pos = 0

	lengths = [ord(str(c)) for c in myInput] + [17, 31, 73, 47, 23]

	for i in range(0, 64):
		for l in lengths:
			pos = pos % arraySize

			array = reverse_sublist(array, pos, pos + l)
			pos += stepSize
			stepSize += 1
			pos += l

	denseHash = []
	i = 0
	while i * 16 < arraySize:
		x = reduce(operator.xor, array[i * 16 : (i + 1) * 16])
		denseHash.append(int2hex(x))
		i += 1

		
	return ''.join(denseHash)

#lengths = sys.stdin.readline()
#lengths = lengths.split(",")
# lengths = "129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108"
# lengths = list(map(lambda char: ord(char), lengths))
# lengths.extend([17, 31, 73, 47, 23])

myInput = 'flqrgnkx'

print knotHash(myInput)

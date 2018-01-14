import sys
import string

def swap(arr, pos1, pos2):
	tmp = arr[pos1]
	arr[pos1] = arr[pos2]
	arr[pos2] = tmp
	return arr


data = sys.stdin.readline()

data = data.split(",")

AtoPstring = string.ascii_lowercase[:16]
AtoP = []
for c in AtoPstring:
	AtoP.append(c)

mem = []	
x = 0
billion = 1000000000
while x < billion:
	for cmd in data:
		cmd = cmd.strip()
		dance = cmd[0]

		if dance == "s":
			spinAmount = int(cmd[1:])
			AtoP = AtoP[len(AtoP) - spinAmount:]+AtoP[0:len(AtoP) - spinAmount]

		if dance == "x":
			pos1,_,pos2 = cmd[1:].partition("/")
			pos1 = int(pos1)
			pos2 = int(pos2)
			AtoP = swap(AtoP, pos1, pos2)

		if dance == "p":
			val1,_,val2 = cmd[1:].partition("/")
			pos1 = AtoP.index(val1)
			pos2 = AtoP.index(val2)
			AtoP = swap(AtoP, pos1, pos2)

	x += 1
	current = ''.join(AtoP)

	if current not in mem:
		mem.append(current)
	else:
		break

print mem
current = ''.join(AtoP)

index = mem.index(current)
mem = mem[index:]

billionthIteration = (billion % len(mem)) - 1

print mem[billionthIteration]




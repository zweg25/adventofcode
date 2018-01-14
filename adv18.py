import sys

data = sys.stdin.readlines()

registers = {}
frequency = 0
x = 0

while x < len(data):
	line = data[x].strip()
	info = line.split()

	cmd = info[0]
	reg = info[1]

	if reg not in registers:
		registers[reg] = 0

	if cmd == "set":
		if info[2] in registers:
			registers[reg] = registers[info[2]]
		else:
			registers[reg] = int(info[2])
	if cmd == "add":
		if info[2] in registers:
			registers[reg] += registers[info[2]]
		else:
			registers[reg] += int(info[2])
	if cmd == "mul":
		if info[2] in registers:
			registers[reg] *= registers[info[2]]
		else:
			registers[reg] *= int(info[2])
	if cmd == "mod":
		if info[2] in registers:
			registers[reg] = registers[reg] % registers[info[2]]
		else:
			registers[reg] = registers[reg] % int(info[2])
	if cmd == "snd":
		frequency = registers[reg]
	if cmd == "rcv" and registers[reg] != 0:
		print "Recovered:", frequency
		break
	if cmd == "jgz" and registers[reg] != 0:
		x += int(info[2])
		x -= 1

	x += 1

print x
print registers


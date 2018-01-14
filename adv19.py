import sys

data = sys.stdin.readlines()

x = 0
y = 0
direction = "down"
currentStr = ""
steps = 0

# Find first spot
while data[y][x] == " ":
	x += 1

while True:
	#Get current row
	line = data[y]

	if line[x] == "+":
		if direction == "up" or direction == "down":
			#Check left and right
			if line[x-1] != " ":
				direction = "left"
			else:
				direction = "right"
		elif direction == "left" or direction == "right":
			#Check up and down
			if data[y-1][x] != " ":
				direction = "up"
			else:
				direction = "down"
	elif line[x] != "|" and line[x] != "-":
		currentStr += line[x]

	if direction == "up":
		y -= 1
	if direction == "down":
		y += 1
	if direction == "left":
		x -= 1
	if direction == "right":
		x += 1

	steps += 1

	if data[y][x] == " ":
		break

print currentStr
print steps

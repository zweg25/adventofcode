import sys

data = sys.stdin.readline()

data = data.strip().split(",")

x = 0
y = 0
z = 0

dists = []

for d in data:
  if d == "n":
    y += 1
    z -= 1
  elif d == "s":
    y -= 1
    z += 1
  elif d == "ne":
    x += 1
    z -= 1
  elif d == "sw":
    x -= 1
    z += 1
  elif d == "nw":
    x -= 1
    y += 1
  elif d == "se":
    x += 1
    y -= 1
  dists.append((abs(x) + abs(y) + abs(z)) / 2)

print (abs(x) + abs(y) + abs(z)) / 2
print max(dists)
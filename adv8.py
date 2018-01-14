import sys
import operator

data = sys.stdin.readlines()
ops = { "inc": operator.add, "dec": operator.sub }
comparators = { "<": operator.lt, ">": operator.gt, "<=": operator.le, ">=": operator.ge, "!=": operator.ne, "==": operator.eq}

commands = []
variables = {}

for line in data:
	arr = line.split()
	arr[2] = int(arr[2])
	arr[6] = int(arr[6])
	commands.append(arr)

max_val = 0

for cmd in commands:
	var1 = cmd[0]
	var1_value = 0
	if var1 in variables:
		var1_value = variables[var1]
	else:
		variables[var1] = 0

	var2 = cmd[4]
	var2_value = 0
	if var2 in variables:
		var2_value = variables[var2]
	else:
		variables[var2] = 0

	if comparators[cmd[5]](var2_value, cmd[6]):
		variables[var1] = ops[cmd[1]](var1_value, cmd[2])

	if max_val < variables[var1]:
		max_val = variables[var1]

print max(variables.values())
print max_val
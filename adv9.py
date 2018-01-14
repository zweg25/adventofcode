import sys
import operator

def iterateThrough(text):
	openings = 0
	total = 0
	inGarbage = False
	accepting = True
	debug = False
	cancelledChars = 0
	for char in text:
		if accepting and not inGarbage:
			if char == "<":
				inGarbage = True
			elif char == "!":
				accepting = False
			elif char == "{":
				openings += 1
			elif char == "}":
				total += openings
				openings -= 1
		elif not accepting:
			accepting = True
		elif inGarbage:
			if char == ">":
				inGarbage = False
			elif char == "!":
				accepting = False
			else:
				cancelledChars += 1
		if debug:
			print char
			print "Accepting:", accepting
			print "InGarbage:", inGarbage
			print "openings:", openings
			print "------------------------"

	#return total
	return cancelledChars

data = sys.stdin.readline()

res = iterateThrough(data)

print res


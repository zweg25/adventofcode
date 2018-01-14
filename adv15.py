prevA = 65
prevB = 8921

factorA = 16807
factorB = 48271

divisor = 2147483647


x = 0
ABPairs = []

pairs = 0

top = 40000000
top = 5000000

while x < top:
	prevBinaryA = '{:032b}'.format(prevA)
	prevBinaryB = '{:032b}'.format(prevB)

	rightMostA = str(prevBinaryA)[-16:]
	rightMostB = str(prevBinaryB)[-16:]

	if rightMostA == rightMostB:
		pairs += 1

	prevA = (prevA * factorA) % divisor
	prevB = (prevB * factorB) % divisor

	while prevA % 4 != 0:
		prevA = (prevA * factorA) % divisor
	while prevB % 8 != 0:
		prevB = (prevB * factorB) % divisor

	x += 1
	if x % 100000 == 0:
		print x / 100000

print "Total pairs:",pairs



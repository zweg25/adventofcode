import sys
import re

sys.setrecursionlimit(3000)

class Node(object):

	allNodes = []

	def __init__(self, name, weight, children, balanced = True):
		self.name = name
		self.weight = int(weight)
		self.children = children
		self.balanced = balanced

	@staticmethod
	def setAllNodes(arg):
		allNodes = arg

	def resetChildren(self):
		#If I am last child, find node that matches my name
		self.children = [x for x in self.children if x != '']
		if not self.children:
			for x in Node.allNodes:
				if x.name == self.name:
					return x
		else:
			newChildren = []
			for c in self.children:
				for x in Node.allNodes:
					if x.name == c:
						currentNode = x
				currentNode.resetChildren()
				newChildren.append(currentNode)
			self.children = newChildren
			return self


	def sumWeights(self):
		# If empty
		if not self.children:
			return self.weight

		total = self.weight
		for childNode in self.children:
			total += childNode.sumWeights()

		return total

	def findImbalance(self):
		if not self.children:
			print "got to nothing"
			return "NOTHING"

		weights = []
		for childNode in self.children:
			weights.append(childNode.sumWeights())

		print self.name, "-", self.weight
		print weights
		print "-----------"

		#all weights are the same
		if all(weight == weights[0] for weight in weights):
			return self.name

		from collections import Counter
		counter = Counter(weights)
		oddWeight = min(counter, key=counter.get)
		
		for childNode in self.children:
			if childNode.sumWeights() == oddWeight:
				x = childNode.findImbalance()
				if x != "NOTHING":
					return x




data = sys.stdin.readlines()
Nodes = []
Childs = []
for s in data:
	num = s[s.find("(")+1:s.find(")")] 
	name,_,_ = s.partition(' ')
	_,_,after = s.partition(' -> ')
	children = re.split(' |, |\n',after)

	Nodes.append(Node(name, num, children))
	Childs.extend(children)

Childs = sorted(list(set(Childs)))

for n in Nodes:
	if not(any(n.name == c for c in Childs)):
		bottomNode = n

#print bottomNode.name

Node.allNodes = Nodes
bottomNode.resetChildren()
print bottomNode.findImbalance()




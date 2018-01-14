import sys

total = 0
for line in sys.stdin:
    row = line.split()
    # if len(row) == len(set(row)):
    # 	total+=1
    valid = True
    for word in row:
    	anagrams = list(filter(lambda x: sorted(x) == sorted(word), row))
    	if len(anagrams) > 1:
    		valid = False
    		break;
    if valid:
    	total+=1

print total

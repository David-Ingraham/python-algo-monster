input = [0,0,1,1,1,2,2]

s = 0
f = 1

#two pointers


while (f <= len(input)):
	curr = input[s]
	next = input[f]

	if curr == next:
		input.pop(next)

	else:
		s = s +1
		f = s +1

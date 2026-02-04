input = [False, False,False, False, True, True, True]


l = 0
r = len(input) - 1

b=-1
while l <= r:

	m = (l+r) //2

	if input[m]:
		b = m

		r = m -1

	else:
		l = m+1

print(b)

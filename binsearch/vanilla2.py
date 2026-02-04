input = [1,22,3,444,678,44444,100000]


t = 678

l = 0

r = len(input) -1

while l <= r:

	m = (l + r ) //2

	if input[m] == t:
		print(m)
		break

	if input[m] < t:
		l = m +1
	else:
		r = m -1

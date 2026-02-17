input = [1,2,3,4,5,6,77,88,99,99999]


t = 99999


l = 0 

r = len(input) -1

while l <=r:

	m = (l+r) //2

	if input[m] ==t:
		print(m)
		break

	if input[m] < t:
		l = m +1
	else:
		r = m -1
		




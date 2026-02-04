input =[1,2,3,4,5,66,77,88,99,100]

t=2

l = 0 

r = len(input) -1

while l <= r:

	m = (l+r) //2

	if input[m] == t:
		print(m)
		break

	if input[m] < t:
		l = m +1

	else:

		r  = m -1
		

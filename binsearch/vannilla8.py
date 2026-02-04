input = [1,2,3,44,55,66,77,99,1000000]


t = 77

l = 0

r = len(input)-1

#print indexi of target value
while l <=r:

	m = (l+r)//2

	if input[m] == t:
		print(m)
		break

	if input[m] < t:
		l = m +1
	else:
		r = m-1




	

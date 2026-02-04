input = [1,2,3,4,5,6,77,77,77,77,88,88,99,100]



l =0 

r = len(input)-1
t = 77
b = -1
while l <= r:
	m = (l +r) //2
	
	if input[m] <= t:
		if input[m] ==t:
			b = m 
		r = m -1 
	else:
		l = m +1


print(b)

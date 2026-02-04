input = [8,9,9.5,9.8,11,13]



#find first input[index] > t

t = 10

#should be index == 1

b = -1
l = 0 

r = len(input) -1

while l <= r:

	m = (l+r)//2

	if input[m] >= t:
		b = m
		r = m -1
	else:
		l = m +1

print(b) 

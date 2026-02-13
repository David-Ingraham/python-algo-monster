input = [0,0,0,1,1,1,2,2,2,3,4]


l = 0

r = len(input)-1

b = 0
t=2
while l <=r:

	m = (l+r) //2

	if input[m] == t:
		b =m

	if input[m] < t:
		l = m +1

	else:
		r = m-1

print(b)






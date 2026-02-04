input=[1,1,1,2,2,2,33,33,44,55]
t=2
b =0
l = 0
r = len(input)-1
while l <=r:
	m = (l+r)//2
	if input[m] <= t:
		if input[m] == t:
			b = m
		l = m +1

	else:
		r = m -1


print(b)

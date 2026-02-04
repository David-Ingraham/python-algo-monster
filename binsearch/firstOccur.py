

#position of first target value w dupes

input = [1,1,1,23,44,44,55,55,80,80,9999]


t= 80
l = 0
r = len(input) - 1
b=-1
while l <= r:
	m = (l +r) //2

	if input[m] >= 55:
		if input[m] == t:
			b = m
		r = m -1

	else:
		l = m +1

print(b)


input = [1,4,6,7,22,55,75,79]


t =79

l =0
r = len(input) -1

while l <= r:

	m = (l+r)//2

	if input[m] == t:
		print(m)
		break

	if input[m] < t:
		l = m+1

	else:
		r = m-1

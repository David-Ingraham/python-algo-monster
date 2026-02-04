#find the sqrt of the target using bin search on srted list


t = 36

input = [i for i in range(0,t+1)]

l = 0

r = t


while l <= r:

	m = (l+r) //2

	if input[m] ** 2 == t:
		print(m)
		break

	if input[m] ** 2 > t:
		r = m -1

	else:
		l = m + 1

 



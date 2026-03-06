arr = [1,1,1,2,2,3,3,4,4,5,66,77]

t = 1

l = 0
r = len(arr) -1
b =0
while l <= r:

	m = (l+r) //2

	if arr[m] == t:
		b = m 
		
	if arr[m] < t:
		l = m +1

	else:
		r = m -1



print(b)
	

	

	







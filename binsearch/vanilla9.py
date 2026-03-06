arr= [0,1,2,3,4,55,66,7777,10000]


l = 0

r = len(arr) -1
t= 3

while l <= r:


	m = (l+r) //2

	if arr[m] == t:
		print(m)
		break;
	if arr[m] < t:
		l = m +1
	else:
		r = m -1


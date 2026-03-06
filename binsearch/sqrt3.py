


t =25 


l = 0

r = t-1


arr = [i for i in range(1,t+1)]

print(arr)

while l <= r:

	m = (l+r) //2

	if arr[m] ** 2 == t:
		print(arr[m])
		
		break


	if arr[m] ** 2 < t:
		l = m +1

	else:
		r = m -1







	

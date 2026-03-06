arr = [0,0,4,6,9]

t = 9


l = 0

r = len(arr) -1


while l < r:

	if arr[l] + arr[r] == t:

		print(l, r)
		break;


	if arr[l] + arr[r] > t:

		r = r -1

	else:

		l = l +1





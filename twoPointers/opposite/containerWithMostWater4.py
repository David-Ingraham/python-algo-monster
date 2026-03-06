arr = [1,3,5,33,5,77,2,4]




l = 0

r = len(arr)-1

curr_max = 0
res_l = 0
res_r = 0

while l <=r:

	area = min(arr[r], arr[l]) * (r-l)

	if area > curr_max:

		curr_max=area
		res_l = l
		res_r = r


	if arr[r] > arr[l]:
		l +=1

	else:
		r -=1




print(arr)
print(f"Left index is {res_l} and right index is {res_r}")
		





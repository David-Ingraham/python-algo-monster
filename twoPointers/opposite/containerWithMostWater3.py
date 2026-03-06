arr =[1,40,4,6,3,90,10]
l = 0

r = len(arr) -1

max_area = 0
index_candL = 0
index_candR = 0
while l <=r:

	curr = min(arr[l], arr[r]) * (r-l)
	print(curr)
	if curr > max_area:
		max_area = curr
		index_candL = l
		index_candR = r



	if arr[l] > arr[r]:
		r -=1


	else:
		l+=1





print(arr)
print(index_candL, index_candR)

arr = [1,0,4,5,7,9,5]




l = 0 

r = len(arr) -1

curr_max = 0

cand1 = 0
cnad1 = 0

while l < r:

	area = min(arr[l], arr[r]) * (r -l)

	if area > curr_max:

		curr_max = area
		cand1 = l
		cand2 = r

	if arr[l] < arr[r]:

		l = l +1

	else:

		r = r -1

		
print(cand1, cand2)

print(arr, curr_max)

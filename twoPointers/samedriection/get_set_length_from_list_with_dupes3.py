arr = [1,1,2,2,3,1,3]

print(f"Array before proceesing: {arr}")

s_ptr = 0

f_ptr = 0
print(arr)
while f_ptr < len(arr)-1:
	f_ptr +=1

	if arr[f_ptr] != arr[s_ptr]:
		s_ptr +=1
		arr[s_ptr] = arr[f_ptr]

new_arr = []

for i in range(s_ptr-1):
	new_arr.append(arr[i])		

print(f"Post processing array:{arr}")

print(f"Set of unique elements in array: {arr[:s_ptr-1]}")

print(f"Lenegth of givenarray's set : {len(arr[:s_ptr-1])}")

print(f"new array: {new_arr}")

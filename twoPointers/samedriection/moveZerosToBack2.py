arr = [6,7,5,4,0,0,0,0,3,5,0,0,3,5]


s_ptr = 0
f_ptr = 0
print(arr)
while f_ptr < len(arr) -1:
	f_ptr +=1
	if arr[f_ptr] == 0:
		arr[s_ptr], arr[f_ptr] = arr[f_ptr], arr[s_ptr]
		s_ptr+=1		


print(arr)

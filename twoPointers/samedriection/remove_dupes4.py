arr= [1,0,7,8,1,2,2,3,4,5,5,6]


s =0

print(arr)

for f in range(len(arr)-1):
	
	if arr[s] != arr[f]:
		arr[s] = arr[f]
		s = s +1


print(arr[:s-1])
		
print(arr)

	

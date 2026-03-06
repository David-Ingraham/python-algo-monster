arr = [0,2,2,0,5,5,5,0,0,3,0,0,0]
s= 0
for f in range(len(arr)):
	
	if arr[f] != 0:

		arr[s], arr[f] = arr[f], arr[s]
			
		s = s +1


		
print(arr)


print(arr)	

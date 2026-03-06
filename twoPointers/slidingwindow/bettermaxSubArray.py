arr = [0,1,33,4,60,90]



k = 3


l = 0 

curr_sum = sum(arr[:k])

ans = curr_sum
for r in range(k,len(arr)):

	curr_sum = curr_sum - arr[l]
	curr_sum = curr_sum + arr[r]

	ans = max(ans, curr_sum)
	l = l +1


print(ans)

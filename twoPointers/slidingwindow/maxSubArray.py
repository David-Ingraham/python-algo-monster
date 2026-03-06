arr = [1,100,30,5,6,70]

k = 3 #subarraylenght. so find the sub array with len 3 that has max sum


l = 0 

r = k-1
cur_max_sum = 0
index_cand1=0
index_cand2=0
while r < len(arr):

	if sum(arr[l:r+1]) >  cur_max_sum:

		cur_max_sum = sum(arr[l: r+1])

		index_cand1 = l

		index_cand2 = r

	else:

		l = l +1

		r = r +1


print(f"max subarrayr: {arr[index_cand1:index_cand2+1]}")

arr = [1,2,3,4,555,4,5,98,433,90,4,2,3]


print(arr)

#print([i for i in range(len(arr))])

	
	

x = 3 #max sub-array len

l = 0
r = x -1

curr =sum(arr[l:r])
max_ = 0
candl = 0
candr = 0
while r < len(arr)-1:
	if curr > max_:
		curr == max_
		candr = r
		candl = l
	r +=1
	l+=1
	curr = curr - arr[l]
	curr = curr + arr[r]





print(arr[candl:candr])

	





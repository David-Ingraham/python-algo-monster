


#each number in the input list represents the y value for the indexes x value on a bar chart. 


nums = [2,4,6,3,4,89,33,5,7,2,3,8,100]


#each numberis the height of the bar. which two bars would you pick as wall of a tub to maximize the volume a water?




#volume is really area here, and the max area will be

# min(result1,result2) * (index_of(result2) - index_of(result1)

# or length * width

cand1, cand2, = 0,0

l = 0 

r = len(nums) -1

curr_max_area = 0 

while l < r:


	if min(nums[l], nums[r]) *  (r -l) > curr_max_area:
		curr_max_area = min(nums[l], nums[r]) *  (r -l)
		cand1, cand2 = l ,r
	if nums[l] > nums[r]:
		r = r -1

	else:
		l = l +1




print(cand1,cand2)








	# how do i know when to move the left pointer and when to move the right?

	# is always looking for a larger max the my previous calculation, so I'd want to keep whichever pointer is at the larger wall and shiftthe smaller one in hopes that i find a bigger wall after i move the pointer at the smaller wall

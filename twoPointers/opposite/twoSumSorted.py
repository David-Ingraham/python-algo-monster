


nums = [1,2,3,4,5, 10, 33,44,55,66,90,100]
print(f"last index is {len(nums)-1}")

t = 110

#return indices of nums adding up to target 




l = 0

r = len(nums)-1


while l <=r:


	if nums[l] + nums[r] == t:
		print(l,r)
		break

	if nums[l] + nums[r] < t:

		l = l +1

	else:
		r = r -1




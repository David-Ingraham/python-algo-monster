#find sqrt of n by chekcing midpoint on list of ints 0 -n, check if midpoint^2 equals the target. if out num squared equals the target, than our num ins the suqare root of the target

#if our num^2 is greater than our target, than we move the right pointer to the midpoint, cutting off all the values/possibilites to the right, or larget than our num, the midpoint, our guess or candidate. 

#now we recalculate our midpioint ot be the middle of our list that only contains nums 0 up to half of n. we keep cutting the list in half from the right, cutting off the larger half if the midpoint swaureed is larger than the target

#if the midpoint squared is less than our target than we cut of the bottom half of our list by moving the left pointer up to the mid point. 

#starting with target 36. r at 36, l at 0, mid at 18. check 18 sqaured, larger than target. move r to m, and recalc m so that r is 18, l is still 0, and m is now 9. 

# check if 9 squared is larger than target, it is, so repeate above. l is still 0, r is 9 and m is 4 (m = (l+r) // 2)  // isfloor divioins, cuts of decimal. essential rounds down

#4 squared is less than the target, so this time we want to move the left pointer 1 right of the mid point.  so l is 5, r is 9 and m = 7

#7 is great than target, so r is 7, l is still 5 and m is 6. 

#6 ^2 == 36



t = 100
input = [i for i in range(1,t+1)]
print(input)
l =0
r = t
while l <=r:

	m = (l+r) //2
#	print(f'midpointer is {m}')
	if input[m] ** 2 == t:
		print(input[m])
		break
	if input[m] ** 2 > t:
		r = m -1

#		print(f"right pointer is {r}")
	if input[m] ** 2 < t:
		l = m + 1

		
#		print(f"left pointer is {l}")









	






  

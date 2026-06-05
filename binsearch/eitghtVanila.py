arr = [1,2,3,44,555,666,2927,9000,]

#return index of given number. if not in list return 0
print("Enter num:")
num = int(input())


l = 0

r = len(arr)-1
num_found =0
while l <= r:

	m = (l + r) // 2

	if arr[m] == num:
		print(m)
		num_found = 1
		break

	if arr[m] > num:

		r -= 1
	else:
		l += 1

if num_found == 0:
	print(f"Num: {num}, not in list {arr}")

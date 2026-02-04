input = [0,0,1,1,1,2,2,2]
print(f"orignal list:{input}")
slow_p = 0

for fast_p in range(len(input)):
	if input[slow_p] != input[fast_p]:
		slow_p += 1
		input[slow_p] = input[fast_p]


print(f"len without dupes: {slow_p +1}")

print(f"set of input: {input[:slow_p+1]}") 

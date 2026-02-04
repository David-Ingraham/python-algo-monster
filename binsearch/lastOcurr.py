input = [1,22,33,33,44,55,55,55,66,66,66,777]
t = 33

print(t)
#indexes = [i for i in range(len(input)-1)])

for i in range(len(input)):

	print(f"{i} {input[i]}")
	




l = 0 
r = len(input) -1
b = -1

while l <= r:

	m = (l+r) // 2

	if input[m] <= t:
		if input[m] == t:
			b = m
		l = m + 1
	else:
		r = m - 1
		

	 
print(b)

print(input)
	
	
	

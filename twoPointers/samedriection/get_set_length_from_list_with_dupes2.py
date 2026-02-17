input = [1,1,2,2,3,3, 10,10,10000000]


s = 0

f = 0

while f < len(input)-1:

	f = f +1

	if input[f] != input[s]:
		s = s +1
		input[s] = input[f]

print(input)

print(f' length without dupes is {len(input[0:s+1])} and list wihout dupes is {input[0:s+1]}')




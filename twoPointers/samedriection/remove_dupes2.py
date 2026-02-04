input = [0,0,1,1,1,2,2]
print(input)



l = 0 

r = 1


while (r < len(input)):
	curr_num = input[l]
	next_num = input[r]

	if next_num == curr_num:

		input.pop(next_num)

	else:
		l = l +1
		r = l + 1

print(input) 

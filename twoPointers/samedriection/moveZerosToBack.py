#move all zeros to bakc of list while aminting relative order of non zero elements 



#question for next time you look at this:

#excatly one charecter is off here. find and fix it 

input = [0,0,0,1,0,2,0,0,0,7,0,0]
print(f"pre processed: {input}")
f = 0

s = 0

while f < len(input) -1:

	f = f +1

	if input[f] == 0:
		input[s], input[f] = input[f], input[s]
		s = s +1

	


print(f'post processing: {input}')




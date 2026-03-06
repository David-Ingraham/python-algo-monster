word = "ooooooooo"



l = 0

r = len(word) -1 
v = True

while l <= r:

	if word[l] != word[r]:
		v = False
		break
	l +=1
	r -=1

print(v)


word = "racwwecar"


l = 0

r = len(word) -1


while l <= r:

	if word[r] != word[l]:
		print("not valid")
		break

	else:
		l +=1
		r -=1

print("valid")

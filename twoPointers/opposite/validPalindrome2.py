
word = "abbba"

is_valid = True
l = 0
r =len(word) -1


while l < r:

	if word[l] != word[r]:
		is_valid = False
		break;
	else:
		l = l +1
		r = r-1


print("is palindrom" if is_valid else "is not palindrome")

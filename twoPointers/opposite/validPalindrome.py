


word: str = "raceca"


is_valid = True

l = 0

r = len(word) -1


while l < r:

	if word[l] != word[r]:

		is_valid = False
		break

	l = l +1
	r = r -1



print(f"is {word} a palindrome? {is_valid}")

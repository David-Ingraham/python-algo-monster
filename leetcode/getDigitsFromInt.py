

print("Enter int:")
a = int(input())
place = 10

while a > 0:
	print(a % place)
	a = a - (a % place)
	place = place ** 10

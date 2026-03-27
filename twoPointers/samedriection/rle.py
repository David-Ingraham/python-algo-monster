st = "77788223311"



s = 0
f = 0
rle_s = ""

for f in range(len(st)):
#while f <= len(st) - 1:
	if st[f] != st[s]:
		rle_s = rle_s + str(f-s)
		rle_s = rle_s + st[s]

		s = f

rle_s = rle_s + str((f-s)+1) + st[s]



print(rle_s)	
		

	

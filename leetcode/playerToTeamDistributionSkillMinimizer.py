players, k = [1,2,3,45,7,4,32,4,7,60], 3

res = []
n = 0
while n <= k:

	res.append([])
	n +=1

#res = [[] for _ in range(k+1)]

for ply in sorted(players, reverse=True):

	_min = map(sum, res)
	res.insert( _min, ply)

print(res)



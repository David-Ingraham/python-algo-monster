"""
Func takes in list as arg, returns a list of indexes from 0 - len(list) -1
lined up with the vals in the given list.
so if this first list bewlo is given, the second list sow is the output.
basically a right padding added based on num length
[1, 333, 45, 4685, 1, 3]
[0, 1,   2,  3,    4, 5 ]
"""
arr = [1,33,45,3,4556,2,399]

def alindPrint(arr): #arr: List[int], func returns String
	res = "["
	for i in range(len(arr)):
		num_wht_spc = len(str(arr[i])) - 1
		res = res + str(i) + ", " + (" " * num_wht_spc)
	#	print(res)
	res = res[:-num_wht_spc]
	#print(res)
	res = res[:-1]
	res = res + "]"
	#print(res)
	return f"{str(arr)}\n{res}"

print(alindPrint(arr))

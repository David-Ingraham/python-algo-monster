#return the start and end index of the target subsequence




#could just do two binary searches for the starting num's index and same for  final num



def bin_search(t:int, test: list):

	l = 0
	r = len(test) -1 

	while l <= r:

		m = (l+r) //2
		if test[m] == t:
			return m

		if test[m] < t:
			l = m +1
		else:
			r = m -1


def main():

	input = [1,2,3,4,5,6,7,8]
	target = [3,4,5]


	print(bin_search(target[0], input), bin_search(target[-1], input))









if __name__ == "__main__":
	main()

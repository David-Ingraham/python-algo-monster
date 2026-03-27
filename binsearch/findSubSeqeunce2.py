arr = [1,2,4,6,7,88,100]

sub = [2,4,6]

def bin_search(arr: list, target: int)-> int:

	l = 0

	r = len(arr) -1

	while l <=r:

		m = (l+r)//2

		if arr[m] == target:
			return m

		if arr[m] < target:
			l = m+1

		else:
			r = m-1






def main():
	print(f"Subsequnce {sub} in array {arr}\n starts on index {bin_search(arr, sub[0])} \n ends on {bin_search(arr, sub[len(sub)-1])}")





if __name__ == "__main__":
	main()




		

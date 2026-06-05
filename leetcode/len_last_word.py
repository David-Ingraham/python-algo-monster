class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        indexes_of_spaces = []
        for i in range(len(s)):
            if s[i] == " ":
                indexes_of_spaces.append(i)
        indexes_of_chars = []

        for i in range(len(s)):
            if s[i] != " ":
                indexes_of_chars.append(i)

        print(f"indexes of chars in string: {indexes_of_chars}")
        print(f"indexes of spaces in string: {indexes_of_spaces}")
        if indexes_of_spaces[-1] < indexes_of_chars[-1]:
            len_last_word = indexes_of_chars[-1] - indexes_of_spaces[-1]
        else:
            len_last_space = indexes_of_spaces[-1] - indexes_of_chars[-1]
            print(f"Len of last space is {len_last_space}")
            indx_before_last_word = indexes_of_spaces[-(len_last_space+1)]
            print(f"index before last word: {indx_before_last_word}")
            len_last_word = (indexes_of_spaces[-len_last_space] - indx_before_last_word) -1
            #len_last_space = indexes_of_spaces[-1] - indexes_of_spaces[-2]
            #len_last_word = indexes_of_chars[-len_last_space-1] - indexes_of_chars[-2]
            #len_last_word = indexes_of_chars[-1] - (len(s) - indexes_of_chars[-1])

            #how do i get the len of spaces at the end? i can do len of the whole string - the last char index
            #calcute len of spaces if s ends in spacees. last space index - char index would equal the len of spaces at the end. then we know how far back we have to push the window

            #len of last word = indexes_of_chars[-len_last_space-1] - indexes_of_chars[-2]
        return len_last_word

def main():

	res = Solution()
	print(res.lengthOfLastWord("   jjjjj    "))


if __name__ == "__main__":
	main()

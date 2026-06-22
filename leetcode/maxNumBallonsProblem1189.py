
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = balloon
        instance = 
        count = 0
        char_dict_word = Counter(word)

        for char in text:
            if char in word:
                instance = instance + char
                text = text.replace(char, )
                print(instance)
                print(text)
            
            if Counter(instance) == char_dict_word:
                count +=1
                instance = 
        return count
            


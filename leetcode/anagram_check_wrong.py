class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _dict ={}
     
        if len(s) != len(t):
            return False
        st = s + t
        for char in st:
            if char not in _dict.keys():
                _dict[char] = 1
            else:
                _dict[char] += 1
        for v in _dict.values():
            if v % 2 != 0:
                print(v)
                return False
        return True

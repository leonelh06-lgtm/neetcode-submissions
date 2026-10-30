class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = {letter: 0 for letter in s}
        freq2 ={letter: 0 for letter in t}
        for letter in s:
            freq1[letter] += 1
        for letter in t:
            freq2[letter] += 1
        return freq1 == freq2
    


        
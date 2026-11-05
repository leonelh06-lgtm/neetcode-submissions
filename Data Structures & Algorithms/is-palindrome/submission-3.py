class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        bad = {" ", ".", ",", "!", "?", "'", ":"}
        for char in s:
            if(char not in bad):
                res += char.lower()
        return res == res[::-1]

        


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        bad = {" ", ",", ".", "?", "!", "'", ":"}
        while(l < r):
            while(l < r and s[l] in bad):
                l += 1
            while(r > l and s[r] in bad):
                r -= 1
            if(s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1
        return True

            

        


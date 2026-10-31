class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if(char == "(" or char == "{" or char == "["):
                stack.append(char)
            if(char == ")" or char == "}" or char == "]"):
                if(len(stack) == 0):
                    return False
                top = stack.pop()
                if(top == "(" and char != ")" or top == "[" and char != "]" or top == "{" and char != "}"):
                    return False

        if(len(stack) > 0):
            return False
        return True

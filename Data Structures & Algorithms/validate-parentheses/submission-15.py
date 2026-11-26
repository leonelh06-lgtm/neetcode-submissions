class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            opening = {"(", "{", "["}
            if(char in opening):
                stack.append(char)
            else:
                if(stack):
                    top = stack.pop()
                    if(char == ")" and top != "("):
                        return False
                    if(char == "]" and top != "["):
                        return False
                    if(char == "}" and top != "{"):
                        return False   
                else:
                    return False   
        if(stack):
            return False
        return True

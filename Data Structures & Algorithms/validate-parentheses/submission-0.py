class Solution:
    @staticmethod
    def isEqual(a: str, b:str) -> bool:
        if(a=='(' and b==')') or (a==')' and b=='('):
            return True
        elif(a=='{' and b=='}') or (b=='{' and a=='}'):
            return True
        elif(a=='[' and b==']') or (b=='[' and a==']'):
            return True
        return False

    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if(s[i] == '(' or s[i]=='{' or s[i]=='['):
                stack.append(s[i])
            elif (s[i] == ')' or s[i]=='}' or s[i]==']'):
                if(len(stack)>0 and self.isEqual(stack[-1], s[i])):
                    stack.pop()
                else:
                    return False
        if(len(stack) > 0):
            return False
        return True

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        for b in s:
            if b=='(' or b=='{' or b=='[':
                stack.append(b)
            if b==')' or b=='}' or b==']':
                if len(stack)==0:
                    return False
                b2=stack.pop()
                if b2+b!='()' and  b2+b!='{}' and b2+b!='[]':
                    return False
        if len(stack)==0:
            return True
        return False

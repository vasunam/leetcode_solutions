class Solution:
    def firstUniqChar(self, s: str) -> int:
        no_char={}
        
        for ch in s:
            no_char[ch]=0
        for ch in s:
            no_char[ch]+=1
            
        for i,ch in enumerate(s):
            if no_char[ch]==1:
                return i
        return -1

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''
        index=0
        strs=list(strs)
        if strs ==None or len(strs)==0:
            return prefix
        
        for char in strs[0]:
            for i in range(len(strs)):
                if index>=len(strs[i]) or char!=strs[i][index]:
                    return prefix
                
            prefix+=char
            index+=1
            
        return prefix

class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        vowels=['A','E','I','O','U','a','e','i','o','u']
        indices=[]
        vowel_list=[]
        
        for i,char in enumerate(s):
            if char in vowels:
                indices.append(i)
                vowel_list.append(char)
                
        indices=indices[::-1]
        
        for i in range(len(indices)):
            s[indices[i]]=vowel_list[i]
            
        return ''.join(s)
            

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count=0
        for i in range(len(word)):
            if word[i].isupper():
                count+=1
                print (count)
                
        if count==len(word) or (count==1 and word[0].isupper()) or count==0:
            return True
        else:
            return False
        

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bcount=0
        count=0
        current=s[0]
        
        for i in range(len(s)):
            current=s[i]
            if(current=='R'):
                count+=1
            if(current=='L'):
                count-=1
            if(count==0):
                bcount+=1
        return bcount

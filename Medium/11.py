class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxm=0
        while(i<j):
            curr=(j-i)*min(height[i],height[j])
            if curr>maxm:
                maxm=curr
                
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
        return maxm

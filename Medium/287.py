class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sum1=sum(list(set(nums)))
        sum2=sum(nums)
        diff=len(nums)-len(set(nums))
        
        if diff==1:
            return sum2-sum1
        
        else:
            result=(sum2-sum1)/diff
            return int(result)

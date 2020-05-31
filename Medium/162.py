class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if nums==[]:
            return None
        if len(nums)==2 :
            if nums[0]>nums[1]:
                return 0
            return 1
        if len(nums)==1:
            return 0
        if max(nums)==nums[0]:
            return 0
        if max(nums)==nums[-1]:
            return len(nums)-1
        
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
                return i

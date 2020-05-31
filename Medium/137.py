class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        setsum=sum(set(nums))*3
        listsum=sum(nums)
        
        return int((setsum-listsum)/2)

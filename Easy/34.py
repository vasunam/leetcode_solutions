class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[]
        final=[]
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)
                
        if len(result)==0:
            return [-1, -1]
        if len(result)==1:
            result.append(result[0])
            return result
        else:
            final.append(result[0])
            final.append(result[-1])
            return final

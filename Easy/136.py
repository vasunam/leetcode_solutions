class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum2=sum(list(set(nums)))*2
        
        return sum2-sum(nums)
    
#     second solution
#         nums.sort()
        
#         for i in range(0,len(nums)-1,2):
#             if nums[i]!=nums[i+1]:
#                 return nums[i]
            
#         return nums[-1]  

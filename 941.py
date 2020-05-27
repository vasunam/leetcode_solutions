class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        peak=0
        going_up=True
 
        if len(A)<3:
            return False
        if A[0]>A[1]:
            return False
        
        for i in range(len(A)-1):
            if A[i]==A[i+1]:
                return False
            
            if A[i]>A[i+1] and going_up:
                peak+=1
                going_up=False
                
            if not going_up and A[i]<A[i+1]:
                return False
        
        if going_up==True:
            return False
        else:
            return True

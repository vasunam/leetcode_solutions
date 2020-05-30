class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            s1=max(stones)
            stones.remove(s1)
            s2=max(stones)
            stones.remove(s2)
            s3=s1-s2
            stones.append(s3)
        return stones[0]

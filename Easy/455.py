class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        s.sort()
        g.sort()
        while g!=[] and s!=[] and min(g)<=max(s) :
            
            for i in range(len(s)):
                if g[0]<=s[i]:
                    g.remove(g[0])
                    s.remove(s[i])                 
                    count+=1
                    break
        return count

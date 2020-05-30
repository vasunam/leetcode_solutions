class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote=list(ransomNote)
        magazine=list(magazine)
        avail_chars={}
        
        for ch in set(magazine):
            avail_chars[ch]=0
        for ch in magazine:
            avail_chars[ch]+=1
        
        for ch in ransomNote:
            if ch in avail_chars and avail_chars[ch]>=1:
                avail_chars[ch]-=1
            else:
                return False
        return True

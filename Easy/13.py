class Solution:
    def romanToInt(self, s: str) -> int:
        value=0
        i=0
        symbols={'I':1,
                 'V':5,
                 'X':10,
                 'L':50,
                 'C':100,
                 'D':500,
                 'M':1000,
                 'IV':4,
                 'IX':9,
                 'XL':40,
                 'XC':90,
                 'CD':400,
                 'CM':900}

        while i<len(s):

            if s[i]=='I' and i+1<len(s) and  s[i+1]=='V':
                value+=symbols['IV']
                i+=2
            elif s[i]=='I' and i+1<len(s) and s[i+1]=='X':
                value+=symbols['IX']
                i+=2
            elif s[i]=='X' and i+1<len(s) and s[i+1]=='L':
                value+=symbols['XL']
                i+=2
            elif s[i]=='X' and i+1<len(s) and s[i+1]=='C':
                value+=symbols['XC']
                i+=2
            elif s[i]=='C' and i+1<len(s) and s[i+1]=='D':
                value+=symbols['CD']
                i+=2
            elif s[i]=='C' and i+1<len(s) and s[i+1]=='M':
                value+=symbols['CM']
                i+=2
            else:
                value=value+symbols[s[i]]
                i+=1

        return value

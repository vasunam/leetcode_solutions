class Solution:
    def letterComboRecur(self, digits, result, index, current, phone_dict):
        if index==len(digits):
            result.append(current)
            return
        
        letters=phone_dict[digits[index]]
        print(result,current)
        for i in range(len(letters)):
            self.letterComboRecur(digits, result, index+1, current+letters[i], phone_dict)
        
    def letterCombinations(self, digits: str) -> List[str]:
        result=[]
        letters=''
        index=0
        current=''
        phone_dict={
                    '2':'abc',
                    '3':'def',
                    '4':'ghi',
                    '5':'jkl',
                    '6':'mno',
                    '7':'pqrs',
                    '8':'tuv',
                    '9':'wxyz'}
        
        if digits==None or len(digits)==0:
            return result
        
        self.letterComboRecur(digits, result, index, current, phone_dict)
        return result

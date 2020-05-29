class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        no_list=[]
        
        if n==0:
            return []

        for i in range(1,n+1):
            if i%3!=0 and i%5!=0 :
                no_list.append(str(i))
            if i%3==0 and i%5!=0:
                no_list.append("Fizz")
            if i%5==0 and i%3!=0:
                no_list.append("Buzz")
            if i%3==0 and i%5==0:
                no_list.append("FizzBuzz")
            
                
        return no_list

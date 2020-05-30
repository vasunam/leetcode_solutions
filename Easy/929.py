class Solution:
    def findBase(self, email):
        domain=email.split('@')[1]
        username=email.split('@')[0]
        username=username.replace('.', '') 
        username=username.split('+')[0] 
        return username+'@'+domain
        
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails=set()
        for email in emails:
            uniqueEmails.add(self.findBase(email))
        # print(uniqueEmails)
        return len(uniqueEmails)

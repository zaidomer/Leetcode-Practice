# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for i in range(0, len(emails)):
            uniqueEmails.add(self.format(emails[i]))
        return len(uniqueEmails)

    def format(self, email: str) -> str:
        atIndex = email.find('@')
        localName = email[0:atIndex]
        domainName = email[atIndex:]

        plusIndex = localName.find('+')
        if plusIndex > -1:
            localName =  localName[0:plusIndex]
        localName = localName.replace('.','')

        return localName+domainName

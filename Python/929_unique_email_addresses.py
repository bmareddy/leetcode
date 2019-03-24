class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        parse each email to it base form by applying the rules
        return length of set of the list returned after applying the function emails list
        """
        def parse_local(email):
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            return local.replace('.','')+'@'+domain
        
        return len(set(map(parse_local, emails)))
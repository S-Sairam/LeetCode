class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        val_email=[]
        for i in emails:
            s=i.split("@")
            local_name=s[0]
            domain=s[1]
            if '+' in local_name:         #removes the +
                x = local_name.split("+")
                local_name=x[0]
            if '.' in local_name:         #removes the . 
                x = local_name.split(".")
                local_name=''
                for j in x :
                    local_name+=j
            e1=local_name+"@"+domain
            val_email.append(e1)
        return len((set(val_email)))

# Solution Link https://leetcode.com/problems/unique-email-addresses/submissions/1154231435

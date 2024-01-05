class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.lstrip().rstrip()
        s = s.split()
        a = ''
        for i in s[::-1] :
            a+=i+' '
        return a.rstrip()
  #https://leetcode.com/problems/reverse-words-in-a-string/submissions/1137149187

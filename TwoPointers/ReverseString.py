class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a=[]
        for i in s:
            a.append(i)
        i=0
        while a:
            s[i] = a.pop()
            i+=1
  #https://leetcode.com/problems/reverse-string/submissions/1154171992
  

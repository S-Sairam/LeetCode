class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        checkST={} 
        checkTS={}
        for i,j in zip(s,t):
            if not ((i in checkST) or (j in checkTS)) :
                checkST[i] = j
                checkTS[j] = i                                     
            if i in checkST and checkST[i]==j and j in checkTS and checkTS[j]==i:
                pass
            else : return False
        print(checkST,checkTS)
        return True
  #https://leetcode.com/problems/isomorphic-strings/submissions/1155566288

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=''
        strs = sorted(strs)
        mini=strs[0]
        maxi=strs[-1]
        for i in range(len(strs[0])):
            if mini[:i+1]==maxi[:i+1]:
                result = maxi[0:i+1]
        return result

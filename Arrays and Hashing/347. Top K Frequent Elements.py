class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        retlist=list(sorted(freq.items(),key = lambda x : x[1]))
        r=[]
        for i in retlist[-1:-(k+1):-1]:
            r.append(i[0])
        return r

  # https://leetcode.com/problems/top-k-frequent-elements/submissions/1152447548

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else : count[i]=1
        for i in count:
            if count[i]>(len(nums)/2):
                return i
#      https://leetcode.com/problems/majority-element/submissions/1155593399

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valIndex={}
        for i in range(len(nums)):#i = index
            t=target-nums[i]
            if t in valIndex:
                return [i,valIndex[t]]
            valIndex[nums[i]]=i

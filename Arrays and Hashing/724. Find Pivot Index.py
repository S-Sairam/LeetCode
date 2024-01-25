#https://leetcode.com/problems/find-pivot-index/submissions/1156232977
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0 
        rightsum=sum(nums)
        for i in range(len(nums)):
            rightsum-=nums[i]
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1

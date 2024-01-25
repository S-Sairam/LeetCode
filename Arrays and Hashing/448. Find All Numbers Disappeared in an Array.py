class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(i for i in range(1,len(nums)+1))-set(sorted(nums)))

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1156246705

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        i=1
        while(i in nums):
            i+=1
        return i

https://leetcode.com/problems/first-missing-positive/submissions/1159213270



#the below solution is memmory efficient while the above one is time efficient
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)+2):
            if i in nums:
                nums.remove(i)
            else:
                return i

https://leetcode.com/problems/first-missing-positive/submissions/1159211904

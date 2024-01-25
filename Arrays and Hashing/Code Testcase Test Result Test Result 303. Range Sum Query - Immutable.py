class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:(right+1)])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


#slow speed but very less memmory https://leetcode.com/problems/range-sum-query-immutable/submissions/1156237902

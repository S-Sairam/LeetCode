class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for i in nums1:
            index=nums2.index(i)
            maxn=-1
            for j in range(index,len(nums2)):
                if nums2[j]>i:
                    maxn=nums2[j]
                    break
            result.append(maxn)
        return result

#https://leetcode.com/problems/next-greater-element-i/submissions/1156220317

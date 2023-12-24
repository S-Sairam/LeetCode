# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         nList=[]
#         for i in range(len(arr)-1):
#             arr.pop(0)
#             nList.append(max(arr))
#         nList.append(-1)
#         return nList
#abv code works but gives a time limit exceed
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/submissions/1127076716  (SIMILAR TO NEETCODES SOLUTION)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxOfRight = -1
        for i in reversed(range(len(arr))):
            arr[i], maxOfRight = maxOfRight, max(maxOfRight, arr[i])
        return arr

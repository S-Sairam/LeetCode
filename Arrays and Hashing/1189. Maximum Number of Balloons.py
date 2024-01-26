class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_map = {'b': 0, 'a':0, 'l':0, 'o': 0, 'n':0}
        
        for char in text:
            if char in hash_map:
                hash_map[char] += 1
        
        hash_map['l'] //= 2
        hash_map['o'] //= 2
        return min(hash_map.values())
https://leetcode.com/problems/maximum-number-of-balloons/submissions/1157132591

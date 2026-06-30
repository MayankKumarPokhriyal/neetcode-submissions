class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cons = 0
        for i in nums:
            if i == 1:
                cons = cons+1
                res = max(res,cons)

            else :
                cons = 0
        return res 
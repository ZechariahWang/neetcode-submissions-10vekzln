class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal=float('-inf')

        for i in range(len(nums)):
            currentSum=0
            for j in range(i, len(nums)):
                currentSum+=nums[j]
                if currentSum > maxVal:
                    maxVal=currentSum


        return maxVal


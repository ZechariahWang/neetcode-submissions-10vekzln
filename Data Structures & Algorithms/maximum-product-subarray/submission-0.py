class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        curMin,curMax=1,1

        for n in nums:
            tempMax=n*curMax
            curMax=max(tempMax,n*curMin,n)
            curMin=min(tempMax,n*curMin,n)
            res=max(res,curMax)
        return res
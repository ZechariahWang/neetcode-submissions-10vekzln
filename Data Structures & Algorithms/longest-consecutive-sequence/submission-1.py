class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        hashset=set(nums)

        for n in nums:
            if n-1 not in hashset:
                temp=1
                while n+temp in hashset:
                    temp+=1
                res=max(temp,res)

        return res



 

        
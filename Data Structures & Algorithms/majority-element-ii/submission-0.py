class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_appearance = n // 3

        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = numbers.get(nums[i], 0) + 1

        res = []
        for i, amount in numbers.items():
            if amount > max_appearance:
                res.append(i)


        return res

        
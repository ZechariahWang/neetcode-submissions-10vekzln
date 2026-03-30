class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkedNumbers = set()

        for i, n in enumerate(nums):
            if not n in checkedNumbers:
                checkedNumbers.add(n)
            else:
                return True

        return False

        
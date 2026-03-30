class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set of numbers that we have checked
        checkedNumbers = set()
        # loop through the entire list, check if each number is in the list
        for num in nums:
            # If the number is in the set, we know we have a duplicate, return true
            if num in checkedNumbers:
                return True

            # add the number to the set
            checkedNumbers.add(num)

        # return false
        return False

        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make a new string as our final solution
        solution = ""
        # loop through the original string
        for c in s:
            # remove every character within the string that isnt alpha numberic
            if c.isalnum():
                # add it to the new string as a lowercase letter
                solution += c.lower()

        # return the new string if it is equal to the newstring reversed
        return solution == solution[::-1]
        
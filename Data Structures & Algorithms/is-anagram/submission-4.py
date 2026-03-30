class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # We need to check if both strings are the same length. 
        # If they aren't, they cant be anagrams

        if len(s) != len(t):
            return False

        # we should loop through ONE of these strings, ill choose s
        # an anagram is the same amount of each character, but in a diff order
        # ill put them in a set so that it removes any duplicates, and only gets the unique characters
        # if the count of each unique character is the same, then we know we have an anagram,, and can return true

        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
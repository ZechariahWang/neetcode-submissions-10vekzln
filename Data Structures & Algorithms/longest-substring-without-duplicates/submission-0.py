class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            characterSet = set()

            for j in range(i, len(s)):
                if s[j] in characterSet:
                    break
                characterSet.add(s[j])
            
            result = max(result, len(characterSet))

        
        return result

        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strategy: 
        # sort all the s in strs
        # the two most diverged strings are at the beginning and the end
        # compare those two only, return the sliced string up to the furthest prefix
        strs.sort()
        final_string=""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                final_string += strs[0][i]
            else:
                break
        
        return final_string



        
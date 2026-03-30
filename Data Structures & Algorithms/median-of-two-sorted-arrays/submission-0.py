class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray=nums1+nums2
        mergedArray.sort()

        if len(mergedArray)%2==0:
            return (mergedArray[len(mergedArray)//2-1]+mergedArray[len(mergedArray)//2])/2
        else:
            return mergedArray[len(mergedArray)//2]
        
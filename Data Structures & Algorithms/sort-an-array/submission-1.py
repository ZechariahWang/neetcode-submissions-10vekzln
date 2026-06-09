class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums, l, m , r):
            left= nums[l:m+1]
            right = nums[m+1: r+1]
            i = l
            j = 0
            k = 0

            # [1,3] [2,4]
            # you always want the pointer to point to the smallest val
            while j < len(left) and k < len(right):
                if  left[j] <= right[k]:
                    nums[i]  = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1

            # dump the rest of the vals for both sides
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                nums[i]= right[k]
                k += 1
                i += 1

        def mergeSort(nums, l, r):
            if l>= r:
                return

            m = (l+r) // 2
            mergeSort(nums, l, m)
            mergeSort(nums, m+1, r)
            merge(nums, l, m, r)

        l, r = 0, len(nums)-1
        mergeSort(nums, l, r)
        return nums
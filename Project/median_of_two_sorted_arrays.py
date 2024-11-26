from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums_list = nums1 + nums2

        sorted_nums_list = sorted(nums_list)

        if len(sorted_nums_list) % 2 != 0:
            median = sorted_nums_list[ int(len(sorted_nums_list) / 2)  ]
        else:
            median = ( (sorted_nums_list[ int(len(sorted_nums_list) / 2) - 1] +
                      sorted_nums_list[ int(len(sorted_nums_list) / 2)]) ) / 2

        return median

solution = Solution()
arr1 = [1, 3]
arr2 = [2]
print(solution.findMedianSortedArrays(arr1, arr2))
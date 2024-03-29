"""
Given two sorted arrays num1 and num2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be 0(log(m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""



from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2
        else:
            return nums[len(nums)//2]
        
if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
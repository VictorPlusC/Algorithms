"""
154. Find Minimum in Rotated Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0

Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""
# Time complexity: O(log N)
# Space complexity: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while left < right:
            pivot = (left+right)//2
            
            if nums[pivot] < nums[right]:
                right = pivot
            elif nums[pivot] > nums[right]:
                left = pivot + 1
            else:
                right -= 1
        return nums[left]

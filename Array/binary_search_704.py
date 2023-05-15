'''
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, 

write a function to search target in nums. 

If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Exampel 1:

Input: nums = [-1,0,3,5,9,12], target = 9

Output: 4

Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2

Output: -1

Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 104

-104 < nums[i], target < 104

All the integers in nums are unique.

nums is sorted in ascending order.

'''

## Original Solution: scan all the list 
## O(n)

class Solution1:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for id, num in enumerate(nums):
            if num == target:
                return id
        return -1

## Binary search [Left, Right]
## O(log2n)
class Solution2:
    def search(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2 
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
        return -1

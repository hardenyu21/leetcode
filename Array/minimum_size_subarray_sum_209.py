'''
209.

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray

whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution,  try coding another solution of which the time complexity is O(n log(n)).

'''


## The naive solution
## O(n^2)
## Error: Time limit exceeded...
class Solution1(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        for size in range(1, len(nums) + 1):
            for id in range(len(nums) + 1 - size):
                if sum(nums[id: id + size]) >= target:
                    return size
        return 0

## Solution2： Sliding window
## O(n)


class Solution2(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        size = float('inf')
        start = 0
        window_sum = 0
        for end in range(len(nums)):
            window_sum += nums[end]
            while window_sum >= target:
                if end - start + 1 <= size:
                    size = end - start + 1 
                window_sum -= nums[start]
                start += 1

        return size if size != float('inf') else 0
    

## Solution 3: 
## O(nlogn) ?

class Solution3(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
    

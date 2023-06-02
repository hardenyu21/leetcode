'''
18.

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

## O(n^3), Hash
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > target / 4:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                map = {}
                for k in range(j + 1, len(nums)):
                    if k > j + 2 and nums[k] == nums[k - 1] == nums[k - 2]:
                        continue
                    d = target - (nums[i] + nums[j] + nums[k])
                    if d in map:
                        result.append([nums[i], nums[j], nums[k], d])
                        map.pop(d)
                    else:
                        map[k] = k
        return result
    

##O(n^3) Two pointer
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > target / 4:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = len(nums) - 1
                while right > left:
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ < target:
                        left += 1
                    elif sum_ > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while right > left and nums[right - 1] == nums[right]:
                            right -= 1
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        
                        right -= 1
                        left += 1

        return result
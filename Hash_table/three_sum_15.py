'''
15.

Given an integer array nums, return all the triplets 

[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

## Brute-force solution
## Time exceeds...
class Solution1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) -1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        new_triplet = [nums[i], nums[j], nums[k]]
                        is_exist = False
                        for triplet in result:
                            if sorted(new_triplet) == sorted(triplet):
                                is_exist = True
                                break
                        if not is_exist:
                            result.append(new_triplet)
        return result
    

## Still time exceeds...
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        two_sum_map = {}
        result = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) - 1):
                two_sum = nums[i] + nums[j]
                if two_sum in two_sum_map:
                    two_sum_map[two_sum].append((i, j))
                else:
                    two_sum_map[two_sum] = [(i, j)]
        
        for (idx, num) in enumerate(nums):
            if -num in two_sum_map:
                for indicies in two_sum_map[-num]:
                    if idx not in indicies:
                        new_triplet = sorted([num, nums[indicies[0]], nums[indicies[1]]])
                        if new_triplet not in result:
                            result.append(new_triplet)
        return result


class Solution3(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            d = {}
            for j in range(i + 1, len(nums)):
                if j > i + 2 and nums[j] == nums[j-1] == nums[j-2]: 
                    continue
                c = 0 - (nums[i] + nums[j])
                if c in d:
                    result.append([nums[i], nums[j], c])
                    d.pop(c) 
                else:
                    d[nums[j]] = j
        return result
    
## Improve...
class Solution4(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return result

            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]
                
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                        
                    right -= 1
                    left += 1
                    
        return result
'''
977.

Given an integer array nums sorted in non-decreasing order, 

return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

Explanation: After squaring, the array becomes [16,1,0,9,100].

After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]

Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104

-104 <= nums[i] <= 104

nums is sorted in non-decreasing order.

Follow up: 

Squaring each element and sorting the new array is very trivial, 

could you find an O(n) solution using a different approach?
'''


'''
Just use the sorted function, square first and sort later

Time complexity: O(nlogn)

Space complexity: O(n)
'''
class Solution1(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [num * num for num in nums]
        return sorted(nums)


'''
Two pointers method: O(n)
'''

class Solution2(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        forward = 0
        backward = len(nums) - 1
        result_index = len(nums) - 1
        result = nums.copy()
        while  result_index >= 0:
            if abs(nums[backward]) >= abs(nums[forward]):
                result[result_index] = nums[backward] * nums[backward]
                backward -= 1
                result_index -= 1
            else:
                result[result_index] = nums[forward] * nums[forward]
                forward += 1
                result_index -= 1
        return result
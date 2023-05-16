'''
27.

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 

The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 

The remaining elements of nums are not important as well as the size of nums.

Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3

Output: 2, nums = [2,2,_,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 2.

It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2

Output: 5, nums = [0,1,4,0,3,_,_,_]

Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.

Note that the five elements can be returned in any order.

It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

0 <= nums.length <= 100

0 <= nums[i] <= 50

0 <= val <= 100
'''


'''
if the number of values equal to val is a, then it will call remove a times,

Time complexity: O(n^2)

Space complexity: O(1)
'''
class Solution1(object):
    def removeElement(self, nums, val):
        k = len(nums)
        while val in nums:
            nums.remove(val)
            k -= 1
        return k, nums
    

'''
Time complexity: O(n)

Space complexity: O(n)
'''
class Solution2(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

'''
Is it possible to improve the space complexity to O(1) ?

Sure!

one pointer starts from the start of the array and goes forward, 

another starts from the end and goes backward.
'''

class Solution3(object):
    def removeElement(self, nums, val):
        backward = len(nums) - 1
        forward = 0
        while forward <= backward:
            if nums[backward] == val:
                backward -= 1
            elif nums[forward] == val:
                nums[forward] = nums[backward]
                backward -= 1
            else:
                forward += 1
        return forward
    
'''
One pointer is fast and another is slow

Compared to solution3, it seems like more efficient

'''

class Solution4(object):
    def removeElement(self, nums, val):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
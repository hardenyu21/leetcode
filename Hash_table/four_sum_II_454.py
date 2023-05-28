'''
454.

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 

return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n

nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
'''

## O(n^4)? Time exceeds...
class Solution1(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        result = 0
        for num1 in nums1:
            for num2 in nums2:
                for num3 in nums3:
                    for num4 in nums4:
                        if num1 + num2 + num3 + num4 == 0:
                            result += 1
        return result

## O(n^2)
class Solution2(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        map = {}
        result = 0
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 in map:
                    map[num1 + num2] += 1
                else:
                    map[num1 + num2] = 1
        
        for num3 in nums3:
            for num4 in nums4:
                if -(num3 + num4) in map:
                    result += map[-(num3 + num4)]
        
        return result

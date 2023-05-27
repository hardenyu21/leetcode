'''
349.

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map1 = [0] * 1001
        map2 = [0] * 1001
        result = []
        for num1 in nums1:
            map1[num1] += 1
        for num2 in nums2:
            map2[num2] += 1
        for idx in range(len(map1)):
            if map1[idx] and map2[idx]:
                result.append(idx)
        
        return result
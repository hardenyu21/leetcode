'''
347.

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        _map = {}
        res = []
        for num in nums:
            if num not in _map:
                _map[num] = 1
            else:
                _map[num] += 1
        pri_queue = []
        for key, value in _map.items():
            heapq.heappush(pri_queue, (value, key))
            if len(pri_queue) > k:
                heapq.heappop(pri_queue)
        
        for _, num in pri_queue:
            res.append(num)
        return res

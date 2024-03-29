"""
416.

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.


"""

from typing import List

class Solution:

    def canPartition1(self, nums: List[int]) -> bool:
        "2-d"
        
        if len(nums) < 2 or sum(nums) % 2:
            return False
        elif max(nums) > sum(nums) // 2:
            return False
        target = sum(nums) // 2
        dp = [[0] * (target + 1) for _ in range(len(nums))]
        for j in range(nums[0], target + 1):
            dp[0][j] = nums[0]
        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                elif dp[i][j - nums[i]] + nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j - nums[i]] + nums[i], dp[i - 1][j])
        return dp[-1][-1] == target

    def canPartition2(self, nums: List[int]) -> bool:

        "2-d"
        if len(nums) < 2 or sum(nums) % 2:
            return False
        elif max(nums) > sum(nums) // 2:
            return False
        target = sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            for j in range(1, target + 1):
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j - nums[i]] or dp[i - 1][j]
        return dp[-1][-1]
    
    def canPartition3(self, nums: List[int]) -> bool:

        "1-d"
        if len(nums) < 2 or sum(nums) % 2:
            return False
        elif max(nums) > sum(nums) // 2:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(len(nums)):
            j = target
            while j >= nums[i]:
                dp[j] = dp[j - nums[i]] or dp[j]
                j -= 1
        return dp[-1]
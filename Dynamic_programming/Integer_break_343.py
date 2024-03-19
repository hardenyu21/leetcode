"""
343.

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 x 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 x 3 x 4 = 36.
 

Constraints:

2 <= n <= 58
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp  = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, len(dp)):
            for j in range(1, i - 1):
                #在每i个对j的循环中，dp[i]的值回动态变化，故加上dp[i]
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

        return dp[-1]

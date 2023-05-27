'''
202.

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:

Input: n = 2
Output: false
 

Constraints:
1 <= n <= 2^31 - 1
'''

## Time exceeds...
class Solution1(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 1:
            last_n = n
            n = str(n)
            sum = 0
            for digit in n:
                sum += pow(int(digit), 2)
            n = sum
            if last_n == n:
                return False
        return True

class Solution2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_list = []

        while n != 1:
            n = str(n)
            sum = 0
            for digit in n:
                sum += pow(int(digit), 2)
            if sum in sum_list:
                return False
            else:
                sum_list.append(sum)
                n = sum
        return True


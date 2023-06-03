'''
541.

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. 

If there are less than 2k but greater than or equal to k characters, 

then reverse the first k characters and leave the other as original.

Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:

Input: s = "abcd", k = 2
Output: "bacd"

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
'''


#too complex
class Solution1(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        n = len(s)
        n_sub = n // (2 * k)
        last = n - n_sub * 2 * k
        result = []
        for i in range(n_sub):
            for j in range(2 * k):
                if j < k:
                    result.append(s[i * 2 * k + k - j - 1])
                else:
                    result.append(s[i * 2 * k + j])

        if last < k:
            for i in range(last):
                result.append(s[n_sub * 2 * k + last - i - 1])
        else: 
            for i in range(last):
                if i < k:
                    result.append(s[n_sub * 2 * k + k - i - 1])
                else:
                    result.append(s[n_sub * 2 * k + i])
        
        return ''.join(result)
    

class Solution2(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        p = 0
        while p < len(s):
            p2 = p + k
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s

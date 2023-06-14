'''
459.

Given a string s, check if it can be constructed by 

taking a substring of it and appending multiple copies of the substring together.

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:

Input: s = "aba"
Output: false

Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''

## Brute-force: O(n^2)
class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sizes = []
        for i in range(1, len(s) + 1):
            if not len(s) % i:
                sizes.append(i)
        
        for size in sizes:
            pattern = s[:size]
            for i in range(size, len(s) - size + 1, size):
                if s[i: i + size] != pattern:
                    break
                if i == len(s) - size:
                    return True
        return False

## O(n)
class Solution2:

    def build_next(self, s: str) -> list:
        next = [0 for _ in range(len(s))]
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[j] != s[i]:
                j = next[j - 1]
            if s[j] == s[i]:
                j += 1
            next[i] = j

    def repeatedSubstringPattern(self, s: str) -> bool:
        next = self.build_next(s)
        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True
        return False
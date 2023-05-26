'''
242.

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 

typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        for item in s:
            if item in s_dict.keys():
                s_dict[item] += 1
            else:
                s_dict[item] = 1
        for item in t:
            if item in t_dict.keys():
                t_dict[item] += 1
            else:
                t_dict[item] = 1
        return s_dict == t_dict
'''
1002.

Given a string array words, return an array of all characters that show up in all strings 

within the words (including duplicates). You may return the answer in any order.

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        word_appear = [[0 for _ in range(26)] for _ in range(len(words))]
        for (idx, word) in enumerate(words):
            for item in word:
                word_appear[idx][ord(item) - ord('a')] += 1

        for idx in range(26):
            word_idx = [word_appear[i][idx] for i in range(len(words))]
            for _ in range(min(word_idx)):
                result.append(chr(ord('a') + idx))
        
        return result
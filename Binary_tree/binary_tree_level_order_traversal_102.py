'''
102.

Given the root of a binary tree, return the level order traversal of its nodes' values.

(i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''

from binary_tree_traversal import TreeNode
from collections import deque

class Solution1:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res = []
        if not root:
            return res
            
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

class Solution2:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        levels = []
        self.helper(root, 0, levels)

        return levels
    
    def helper(self, node, level, levels):

        if not node:
            return 
        if len(levels) == level:
            levels.append([])

        levels[level].append(node.val)
        self.helper(node.left, level + 1, levels)
        self.helper(node.right, level + 1, levels)
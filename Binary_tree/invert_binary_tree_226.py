'''
226.

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''
from binary_tree_traversal import TreeNode
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.right)
                queue.append(node.left)
                node.left, node.right = node.right, node.left
        return root
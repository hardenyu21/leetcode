'''
104.

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 

from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''
from binary_tree_traversal import TreeNode
from collections import deque
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        queue = deque([root])
        while queue:
            depth += 1
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth

class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        
        depth = self.helper(root, 0)

        return depth
    
    def helper(self, root, depth):

        if not root:
            return 0
        
        self.helper(root.left, depth +1)
        self.helper(root.right, depth + 1)
        
        


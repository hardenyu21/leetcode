'''
110.

Given a binary tree, determine if it is  height-balanced

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''
from binary_tree_traversal import TreeNode
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:  
        
        return self.get_height(root) != -1
    
    def get_height(self, node):
        
        if not node:
            return 0
        
        left = self.get_height(node.left)
        right = self.get_height(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1

        

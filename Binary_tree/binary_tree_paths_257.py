'''
257.

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''

from binary_tree_traversal import TreeNode

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> int:
        if not root:
            return []
        stack = [(root, str(root.val))]
        res = []
        while stack:
            node, path = stack.pop()
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
            
            if not (node.left or node.right):
                res.append(path)

        return res
            
            
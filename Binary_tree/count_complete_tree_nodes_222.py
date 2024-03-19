'''
222.

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last,  is completely filled in a complete binary tree, 

and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1
 
Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
'''
##O(n)
from binary_tree_traversal import TreeNode

class Solution1:
    def countNodes(self, root: TreeNode) -> int:
        return self.getNodes(root)

    def getNodes(self, node):

        if not node:
            return 0
        
        leftnum = self.getNodes(node.left)
        rightnum = self.getNodes(node.right)
        treenum = leftnum + rightnum + 1
        return treenum


class Solution2:
    def countNodes(self, root:TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        res = 1
        while stack:
            node = stack.pop()
            if node.left:
                res += 1
                stack.append(node.left)
            if node.right:
                res += 1
                stack.append(node.right)
        
        return res

##Use the property of complete tree
class Solution3:

    def countNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        left = root.left
        right =root.right
        leftdepth = 1
        rightdepth = 1
        while left:
            left = left.left
            leftdepth += 1
        while right:
            right = right.right
            rightdepth += 1
        if leftdepth ==  rightdepth:
            return pow(2, leftdepth) - 1
        
        return self.countNodes(left) + self.countNodes(right) + 1
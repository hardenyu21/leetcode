'''
101.

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
'''
from binary_tree_traversal import TreeNode
from collections import deque
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
    
    def compare(self, left, right):

        if  left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True
        elif left.val != right.val: return False

        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)

        return outside and inside

class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = deque([root.left, root.right])
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if left == None and right!= None: return False
            elif left != None and right == None: return False
            elif left == None and right == None: continue
            elif left.val != right.val: return False

            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        
        return True

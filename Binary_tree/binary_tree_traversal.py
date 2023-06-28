'''

144, 94, and 145

'''
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution1:
    def preorderTraversal(self, root: TreeNode):
        if not root:
            return []
        
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return [root.val] + left + right

class Solution2:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right
    
class Solution3:
    def postorderTraversal(self, root: TreeNode):
        if not root:
            return []
        
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        return  left + right + [root.val]

class Solution4:
    def preorderTraversal(self, root: TreeNode):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            stack.append(node.right)
            stack.append(node.left)
            res.append(node.val)
        return res
    
class Solution5:
    def inorderTraversal(self, root: TreeNode):
        res = []
        stack = []
        current = root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                res.append(current.val)
                current = current.right
        return res


class Solution6:
    def postorderTraversal(self, root: TreeNode):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            stack.append(node.left)
            stack.append(node.right)
            res.append(node.val)
        return res[::-1]


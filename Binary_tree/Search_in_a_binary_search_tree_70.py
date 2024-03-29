"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 

If such a node does not exist, return null.

"""
from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root 
        while node:
            if val > node.val:
                node = node.right
            elif val < node.val:
                node = node.left
            else:
                return node


class Solution2:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        if root.val > val: 
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)

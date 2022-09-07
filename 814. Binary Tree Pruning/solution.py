# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        if root.left != None:
            root.left = self.pruneTree(root.left)
        if root.right != None:
            root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left == None and root.right == None:
            return None
        else:
            return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sumOfLeaves=0
    def isLeaf(self, root):
        if root==None:
            return False
        if root.left==None and root.right==None:
            return True
        else:
            return False
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root==None:
            return self.sumOfLeaves
        if self.isLeaf(root.left):
            self.sumOfLeaves+=root.left.val
            
        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)
        return self.sumOfLeaves

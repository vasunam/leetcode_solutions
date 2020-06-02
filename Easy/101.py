# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric2(self, left, right):
        if left==None or right==None:
            return left==right
        
        if left.val!=right.val:
            return False
        
        return self.isSymmetric2(left.left, right.right) and self.isSymmetric2(left.right, right.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        
        return self.isSymmetric2(root.left, root.right)

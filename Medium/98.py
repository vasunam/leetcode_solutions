# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isGudTree(self, root, ll, ul):
        if root==None:
            return True
            
        if (root.left!=None and root.left.val>=root.val) or (root.right!=None and root.right.val<=root.val):
            return False

        if root.val>=ul or root.val<=ll:
            return False
        
        return self.isGudTree(root.left, ll, root.val) and self.isGudTree(root.right, root.val, ul)
        
        
        
    def isValidBST(self, root: TreeNode) -> bool:
        
        return self.isGudTree(root, -99999999999999999, 999999999999999999)

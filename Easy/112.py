# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root):
        if root.left==None and root.right==None:
            return True
        else:
            return False
        
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        result=False
        if root==None:
            return
        
        
        sum-=root.val
        print(sum,root.val,self.isLeaf(root))
        if sum==0 and self.isLeaf(root):
            return True
        
        if self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum):
            return True    
        
        
        if sum!=0  and self.isLeaf(root):
            return
        return False

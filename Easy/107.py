# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printLevel(self, root, height, result):
        if height==0:
            result.append(root.val)
        if root.left:
            self.printLevel(root.left, height-1, result)
        if root.right:
            self.printLevel(root.right, height-1, result)
        
    def findHeight(self, root):
        if root==None:
            return 1
        return 1+max(self.findHeight(root.left),self.findHeight(root.right))
        
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result=[]
        
        if root==None:
            return result
        
        height=self.findHeight(root)-1
        for i in range(height-1,-1,-1):
            level=[]
            self.printLevel(root, i, level)
            result.append(level)
            
        return result

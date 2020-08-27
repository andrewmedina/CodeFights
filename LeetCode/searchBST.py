# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val == val:
            return root
        leftsearch = self.searchBST(root.left,val)
        rightsearch = self.searchBST(root.right,val)
        if leftsearch:
            return leftsearch
        elif rightsearch:
            return rightsearch
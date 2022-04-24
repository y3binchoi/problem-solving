# 938. Range Sum of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0

    def rangeSumBST(self, node: Optional[TreeNode], L: int, R: int) -> int:
        if node:
            if L <= node.val <= R:
                self.sum += node.val
            self.rangeSumBST(node.left, L, R)
            self.rangeSumBST(node.right, L, R)
        return self.sum

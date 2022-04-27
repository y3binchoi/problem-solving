# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, node: Optional[TreeNode], L: int, R: int) -> int:
        if node:  # node가 존재하면
            temp = node.val if L <= node.val <= R else 0
            left = self.rangeSumBST(node.left, L, R)
            right = self.rangeSumBST(node.right, L, R)
            return temp + \
                   (left if left is not None else 0) + \
                   (right if right is not None else 0)

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

#     1 -> NULL
#    / \
#  2  -> 3 -> NULL
# /  \   / \
# 4->5->6->7 -> NULL

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root.left is not None:
            root.left.next = root.right
            self.connect(root.left)
            self.connect(root.right)

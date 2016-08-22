## 104. Maximum Depth of Binary Tree(EASY)
##
## Given a binary tree, find its maximum depth.
##
## The maximum depth is the number of nodes along the
## longest path from the root node down to the farthest leaf node.

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

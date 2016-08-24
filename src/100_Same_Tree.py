## 100. Same Tree(EASY)
##
## Given two binary trees, write a function to check if they are equal or not.
##
## Two binary trees are considered equal if they are structurally identical
## and the nodes have the same value.
##
## Subscribe to see which companies asked this question
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if q and p:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif q is None and p is None: # can use 'p is q' to judge if p and q are the same object
            return True
        else:
            return False

# simple solution on leetcode
def isSameTree_(self, p, q):
    if q and q:
        return p.val == q.val and self.isSameTree_(p.left, q.left) and self.isSameTree_(p.right, q.right)
    return q is p # object identify

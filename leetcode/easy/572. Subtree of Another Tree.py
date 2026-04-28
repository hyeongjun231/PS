# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, tree, sub):
        if not tree and not sub:
            return True
        if (tree and not sub) or (not tree and sub):
            return False
        if tree.val != sub.val:
            return False
        if not self.isSame(tree.left, sub.left):
            return False
        if not self.isSame(tree.right, sub.right):
            return False
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.val == subRoot.val:
                if self.isSame(cur, subRoot):
                    return True

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return False
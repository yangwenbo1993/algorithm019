# 二叉树的最近公共祖先
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNod, q: TreeNode) -> 'TreeNode':
        if root == None:
            return None
        if root == p or root ==q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right =self.lowestCommonAncestor(root.right,p,q)
        if left == None:
            return right
        if right == None:
            return left
        if left and right:
            return root
        return None




# 组合
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def recall(n, k, start, result, subset):
            if len(subset) == k:
                result.append(subset[:])
                return
            for i in range(start, n+1):
                if k-len(subset) > n-i+1:
                    break
                subset.append(i)
                recall(n, k, i+1, result, subset)
                subset.pop()
        recall(n, k, 1, result, [])
        return result
#二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        self.result = []
        self.inorder(root)

        return self.result

    def inorder(self, root: TreeNode):
        if not root:
            return
        self.inorder(root.left)
        self.result.append(root.val)
        self.inorder(root.right)


#二叉树的前序遍历
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        self.result = []
        self.preorder(root)

        return self.result

    def preorder(self, root: TreeNode):
        if not root:
            return
        self.result.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)




# 二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




# 字母异位词分组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> list:
        result = {}
        for word in strs:
            key = tuple(sorted(word))
            result[key] = result.get(key,[])+[word]
        result = list(result.values())

        return result







# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        list = []
        stack = []
        while root or stack:
            if root:
                list.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return list
        
    def recurisive_preorder(self, root, list=[]):
    	if root:
    		list.append(root.val)
    		self.recurisive_preorder(root.left, list)
    		self.recurisive_preorder(root.right, list)
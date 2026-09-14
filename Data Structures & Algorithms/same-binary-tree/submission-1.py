# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        res_p = []
        res_q = []
        def preorder_p(node):
            if node != None:
                res_p.append(node.val) 
                preorder_p(node.left)
                preorder_p(node.right)
            else:
                res_p.append("null")
            return res_p
        res_p = preorder_p(p)

        def preorder_q(node):
            if node != None:
                res_q.append(node.val) 
                preorder_q(node.left)
                preorder_q(node.right)
            else:
                res_q.append("null")
            return res_q
        res_q = preorder_q(q)
        return res_p == res_q 

#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-04 14:01 
# @Author : magician 
# @File : 145_easy.py 
# @Software: PyCharm



# 145. 二叉树的后序遍历
# 给定一个二叉树，返回它的 后序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# 1
# \
# 2
# /
# 3
#
# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        def helper(root):
            if not root:
                return

            helper(root.left)
            helper(root.right)
            res.append(root.val)

        res=[]
        helper(root)
        return res



#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-29 21:05 
# @Author : magician 
# @File : 107.py 
# @Software: PyCharm


# 107. 二叉树的层序遍历 II
# 给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 3
# / \
#     9  20
# / \
#     15   7
# 返回其自底向上的层序遍历为：
# [
#     [15,7],
#     [9,20],
#     [3]
# ]

# 思路二：递归/DFS
#  按照层序遍历得到结果后，再反转即可

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        def dfs(root,deep):
            if not root:
                return
            if len(res)==deep:
                res.append([])

            res[deep].append(root.val)

            dfs(root.left,deep+1)
            dfs(root.right,deep+1)

        res=[]
        dfs(root,0)
        return res[::-1]
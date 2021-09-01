#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-01 21:38 
# @Author : magician 
# @File : 404.py 
# @Software: PyCharm


# 404. 左叶子之和
# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
# 3
# / \
#     9  20
# / \
#     15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        #注意这里用self.res而非res。
        self.res=0
        def dfs(root):
            #若根节点不存在，则结果为0
            if not root:
                return 0
            #若左节点存在，但左节点无子节点（即左叶子节点的定义）
            #若有左叶子节点，就把值给加上
            if root.left and not root.left.left and not root.left.right:
                self.res+=root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res


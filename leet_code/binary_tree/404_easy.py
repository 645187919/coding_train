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
        #注意这里用self.res而非res。是某实例的变量，可以在类内部使用
        self.res=0
        def dfs(root):
            #若子树根节点不存在，则结果为0
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

    #思路：得到所有的左叶子节点，然后累加
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        #1、递归函数的参数及返回值。返回所有的左叶子节点。

        def helper(root):
            #若子树的根节点不存在直接终止；
            if not root:
                return
            #若节点存在则观察做节点是否是叶子节点
            if root.left and (not root.left.left and not root.left.right):
                res.append(root.left.val)

            helper(root.left)
            helper(root.right)
        res=[]
        helper(root)
        return sum(res)

        #2、递归终止条件：找到左叶子节点则进入队列后终止，若非左叶子节点，则直接终止；

        #3、递归函数单层逻辑：分别找左右子树的左叶子节点。

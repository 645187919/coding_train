#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-30 22:06 
# @Author : magician 
# @File : 111_easy.py 
# @Software: PyCharm

# 111. 二叉树的最小深度
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明：叶子节点是指没有子节点的节点。
#
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
# 示例 2：
#
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
# 提示：
#
# 树中节点数的范围在 [0, 105] 内
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        #若左节点为空，则返回1+右节点最小深度
        elif not root.left:
            return 1+self.minDepth(root.right)
        #若右节点为空，则返回1+左节点最小深度
        elif not root.right:
            return 1+self.minDepth(root.left)
        #若左右节点都不为空。若直接用该等式，会把空节点当做最小的深度包含进来。
        #如[2,null,3,null,4,null,5,null,6] 返回值就为1，实质为5
        else:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
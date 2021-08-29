#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-29 21:28 
# @Author : magician 
# @File : 103_medium.py 
# @Software: PyCharm

# 103. 二叉树的锯齿形层序遍历
# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
# 3
# / \
#     9  20
# / \
#     15   7
# 返回锯齿形层序遍历如下：
#
# [
#     [3],
#     [20,9],
#     [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(root,deep):
            if not root:
                return
            if len(res)==deep:
                res.append([])
            if deep%2==0:
                res[deep].append(root.val)
            else:
                #很巧妙的利用list的insert方法来改变插入值的顺序
                res[deep].insert(0,root.val)

            dfs(root.left,deep+1)
            dfs(root.right,deep+1)

        res=[]
        dfs(root,0)
        return res
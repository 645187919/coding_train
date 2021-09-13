#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-30 21:49 
# @Author : magician 
# @File : 104_easy.py 
# @Software: PyCharm


# 104. 二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
# 3
# / \
#     9  20
# / \
#     15   7
# 返回它的最大深度 3 。

#思路:遍历存储每个节点的深度，然后获取最大值。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res=[]

        def dfs(root,deep):
            if not root:
                return
            res.append(deep)
            deep+=1
            dfs(root.left,deep)
            dfs(root.right,deep)

        dfs(root,1)
        print(res)
        return 0 if len(res)==0 else max(res)


#将求深度的问题转化为求当前节点深度1+孩子节点的深度的最大值。依次递归。
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))





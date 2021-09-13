#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-29 16:53 
# @Author : magician 
# @File : 144_easy.py 
# @Software: PyCharm

# 144. 二叉树的前序遍历
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
#

# 示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
# 示例 2：
# 输入：root = []
# 输出：[]
# 示例 3：
# 输入：root = [1]
# 输出：[1]
# 示例 4：
# 输入：root = [1,2]
# 输出：[1,2]
# 示例 5：
# 输入：root = [1,null,2]
# 输出：[1,2]
#
# 提示：
# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        def preorder(root):
            #终止条件
            if root==None:
                return
            #前序遍历（root，left,right）
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        #全局list
        res=[]
        preorder(root)
        return res




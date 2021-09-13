#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-29 17:03 
# @Author : magician 
# @File : 94_easy.py 
# @Software: PyCharm

# 94. 二叉树的前序遍历
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        res=[]
        inorder(root)
        return res
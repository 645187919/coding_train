#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-31 21:41 
# @Author : magician 
# @File : 110.py 
# @Software: PyCharm
#
# 110. 平衡二叉树
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
#
# 示例 1：
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
# 示例 2：
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
# 示例 3：
#
# 输入：root = []
# 输出：true
#
# 提示：
# 树中的节点数在范围 [0, 5000] 内
# -104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#自底向上
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        self.res = True
        def helper(root):
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            #print(right, left)
            if abs(right - left) > 1:
                self.res = False
            #为了记录层数
            return max(left, right)
        helper(root)
        return self.res

#自顶向下
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.height(root.right)-self.height(root.left))<2 \
               and self.isBalanced(root.left) and self.isBalanced(root.right)
    # 求高度
    def height(self, node):
        if not node:
            return 0
        return 1+max(self.height(node.right),self.height(node.left))

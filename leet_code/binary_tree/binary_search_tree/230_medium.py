#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-04 15:25 
# @Author : magician 
# @File : 230_medium.py 
# @Software: PyCharm

# 230. 二叉搜索树中第K小的元素
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
# 示例 1：
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
# 示例 2：
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3

# 提示：
#
# 树中的节点数为 n 。
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #中序遍历，然后获取第k小数.
        res=[]
        def mind_sort(root):
            if not root:
                return
            mind_sort(root.left)
            res.append(root.val)
            mind_sort(root.right)
        mind_sort(root)
        #print(res)

        return res[k-1] if len(res)>=k else None
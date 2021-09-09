#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-31 22:10 
# @Author : magician 
# @File : 112_easy.py 
# @Software: PyCharm

# 112. 路径总和
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在根节点到叶子节点的路径，
# 这条路径上所有节点值相加等于目标和 targetSum 。
# 叶子节点是指没有子节点的节点。
#
# 示例 1：
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
# 示例 2：
# 输入：root = [1,2,3], targetSum = 5
# 输出：false
# 示例 3：
# 输入：root = [1,2], targetSum = 0
# 输出：false
# 提示：
# 树中节点的数目在范围 [0, 5000] 内
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

#思路：https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-de-si-chong-jie-fa-dfs-hui-su-bfs-/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)



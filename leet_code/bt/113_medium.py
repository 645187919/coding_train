#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-02 20:24 
# @Author : magician 
# @File : 113_easy.py 
# @Software: PyCharm


# 113. 路径总和 II
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 叶子节点 是指没有子节点的节点。
# 示例 1：
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
# 示例 2：
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
# 示例 3：
# 输入：root = [1,2], targetSum = 0
# 输出：[]
# 提示：
# 树中节点总数在范围 [0, 5000] 内
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
#思路参考：https://leetcode-cn.com/problems/path-sum-ii/solution/tao-mo-ban-er-cha-shu-wen-ti-de-dfs-he-bfs-jie-fa-/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, sum, res, [])
        return res

    def dfs(self, root, sum, res, path):
        if not root: # 空节点，不做处理
            return

        if not root.left and not root.right: # 叶子节点
            if sum == root.val: # 剩余的「路径和」恰好等于叶子节点值
                res.append(path + [root.val]) # 把该路径放入结果中
        #如何记录路径
        self.dfs(root.left, sum - root.val, res, path + [root.val]) # 左子树
        self.dfs(root.right, sum - root.val, res, path + [root.val]) # 右子树

#另一种写法（注意tmp + [root.val]的位置以及写法，换成其他的跑不通...）
class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        #用tmp去记录每次的路径
        def helper(root, tmp, sum_):
            if not root:
                return
            if not root.left and not root.right and sum_ - root.val == 0:
                tmp += [root.val]
                res.append(tmp)
            helper(root.left, tmp + [root.val], sum_ - root.val)
            helper(root.right, tmp + [root.val], sum_ - root.val)
        res = []
        helper(root, [], sum_)
        return res





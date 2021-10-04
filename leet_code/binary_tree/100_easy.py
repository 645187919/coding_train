#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-31 20:35 
# @Author : magician 
# @File : 100_easy.py 
# @Software: PyCharm

# 100. 相同的树
# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# 示例 1：
# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
# 示例 2：
# 输入：p = [1,2], q = [1,null,2]
# 输出：false
# 示例 3：
# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false

# 提示：
# 两棵树上的节点数目都在范围 [0, 100] 内
# -104 <= Node.val <= 104

#思路：递归+DFS。
# 注意先思考递归的终止条件：1、两个节点的值不等。两个节点若一个存在一个不存在，两个节点为空。
#否则分别递归的比较左右两个孩子节点。

# 参考：https://leetcode-cn.com/problems/same-tree/solution/xie-shu-suan-fa-de-tao-lu-kuang-jia-by-wei-lai-bu-/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #判断特征条件
        #若p和q都为空：叶子节点，返回true；
        if not p and not q:
            return True
        #如果两节点一个为空一个不为空（上面剔除了两节点都为None的情况）；
        elif not p or not q:
            return False
        #停止条件：若两个比较节点的值不同，则停止
        if p.val!=q.val:
            return False
        #否则就递归的比较左右两个孩子节点的值
        return self.isSameTree(p.left,q.left) & self.isSameTree(p.right,q.right)


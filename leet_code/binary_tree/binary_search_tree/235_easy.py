#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-02 21:43 
# @Author : magician 
# @File : 235_easy.py 
# @Software: PyCharm

# 235. 二叉搜索树的最近公共祖先
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

# 示例 1:
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 示例 2:
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。


#注意二叉树的特性和本题的结合点：
#左边节点比父节点小，右边节点比父节点大。若p和q都比根节点大或小，则代表p和q在同一侧，
# 则需要接着和root的根节点对比，不断递归。
# 若p和q一个比根节点大一个比根节点小，则代表在根节点两侧，则最小父节点为根节点。

# 思考过程
# 题目要求为最近的公共祖先，首先想到的是普通二叉树的做法，分别记录从root遍历到 p q节点的祖先，对比得到最近公共祖先
# 但是这道题为BST，分析BST特征，左树比当前节点小，右树比当前节点大。可以想到，我们可以容易的判断p,q在当前节点的哪一侧。
# 如果再同侧，则再往下层递归，如在两侧，则返回当前节点
# 注意一下边界条件，得出代码：

#参考：
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/solution/python3-di-gui-si-kao-guo-cheng-by-terryli/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root

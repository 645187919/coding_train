#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-04 15:46 
# @Author : magician 
# @File : 236_easy.py 
# @Software: PyCharm

# 236. 二叉树的最近公共祖先
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 示例 1：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
# 示例 2：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
# 示例 3：
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
#
# 提示：
#
# 树中节点数目在范围 [2, 105] 内。
# -109 <= Node.val <= 109
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。

#思路口诀：【最近公共祖先】空或搜到即返回。左搜搜，右搜搜。左右都有，那就是你；左没便在右，右没便在左

#参考：
# 1、https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/zhong-xu-bian-li-bian-yi-ge-kou-jue-bang-zhu-li-ji/
# 2、https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        #由于二叉树是无序的，所以只能区分几种情况：
        #若root为空或者为p或q，则返回root
        if not root:
            return root
        if root is p or root is q:
            return root
        #查找p或q在左右子树中的情况。
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left
#20211006 updtate
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root,p,q):
            #递归输入，输出
            #递归终止条件
            if not root:
                return
            #root和p，q是否相等
            if root is p or root is q:
                return root
            #递归单层逻辑：
            left=helper(root.left,p,q)
            right=helper(root.right,p,q)
            if left and right:
                return root
            if not left:
                return right
            if not right:
                return left
        return helper(root,p,q)
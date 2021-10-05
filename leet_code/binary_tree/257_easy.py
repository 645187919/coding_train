#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-01 22:00 
# @Author : magician 
# @File : 257_easy.py 
# @Software: PyCharm


# 257. 二叉树的所有路径
# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 叶子节点 是指没有子节点的节点。
# 示例 1：
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
# 示例 2：
# 输入：root = [1]
# 输出：["1"]
# 提示：
# 树中节点的数目在范围 [1, 100] 内
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#思路：依次穷举每种类型，然后写代码（终止条件即为叶子节点）
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res=[]
        def dfs(root,path):
            path+=str(root.val)
            if not root.left and not root.right:
                res.append(path)
            elif not root.left:
                dfs(root.right,path+'->')
            elif not root.right:
                dfs(root.left,path+'->')
            else:
                dfs(root.right,path+'->')
                dfs(root.left,path+'->')
        dfs(root,'')
        return res

    #方法二：若为空节点则return（结束当前递归）。否则只考虑叶子节点的情况，若是则加入res。
    #若不是则记录每个节点的值，依次对左右子树做递归（该代码为深度优先）
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        #1、递归函数的参数及返回结果：path，root；所有的路径。
        def helper(root,path):
            #2、终止条件：子树的根节点为空则终止；

            if not root:
                return
            #3、单层逻辑：对当前路径进行累加，若为叶子节点，则将路径放入列表中，遍历其左右子树
            path=path+str(root.val)
            if not root.left and not root.right:
                res.append(path)
            helper(root.left,path+'->')
            helper(root.right,path+'->')
        res=[]
        helper(root,'')
        return res





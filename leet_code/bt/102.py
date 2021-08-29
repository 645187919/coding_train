#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-29 20:36 
# @Author : magician 
# @File : 102.py 
# @Software: PyCharm

# 102. 二叉树的层序遍历
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

# 示例：
# 二叉树：[3,9,20,null,null,15,7],
# 3
# / \
#     9  20
# / \
#     15   7
# 返回其层序遍历结果：
# [
#     [3],
#     [9,20],
#     [15,7]
# ]

# 思路：广度优先。
# 用队列来存储每层的节点，然后提取每层节点的val值到一个list中。获取当前节点的孩子节点，重复上面的流程。

# 详细参考：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/python3-er-cha-shu-ceng-xu-bian-li-by-jo-nlx3/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #如果root为空则返回空
        if not root:
            return []
        #root是一颗数的根节点
        print(root)
        queue=[root]
        #收集树节点每层的val值
        res=[]
        #queue是一个队列，里面只包含根节点这一个元素
        print(queue)
        while queue:
            #res收集每一层节点的val值
            res.append([node.val for node in queue])
            #ll用于存储每层的节点
            ll=[]
            #对当前层的每个节点遍历
            for node in queue:
                #如果左子节点存在，入队列
                if node.left:
                    ll.append(node.left)
                if node.right:
                    ll.append(node.right)
            #后把queue更新成下一层的结点，继续遍历下一层
            queue=ll
        return res









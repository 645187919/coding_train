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

# 思路一：迭代/BFS
# 层序遍历自然用广度优先搜索(BFS)最合适了
#1、 用队列来保存节点，先进先出，因为题目要求不同层的节点值要分开保存，
# 那while循环里还需要for循环来一次性搞完该层所有节点
#
# 2、对于弹出的节点，将其节点值存入tmp数组，然后左右节点如果存在的话依次加入队列queue中
# 3、每一层遍历完，将tmp加到res中
# 4、返回res

# 思路二：递归/DFS
# 1、因为每层的节点值要分开记录，所以递归的参数除了节点node以外还需要当前层数level
# 2、如果节点已为空，return，结束当前递归分支即可
# 3、如果res的长度已经和当前层数level相等，说明res需要多加个位置了，因为level是res数组的索引，
# 索引是一定比长度要小的，如果相等说明数组长度不够长了，得扩容
# 4、把当前节点加到对应层的数组中去res[level].append(node.val)
# 5、继续依次遍历左右字节点，层数level + 1
# 6、返回res



# 详细参考：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/python3-er-cha-shu-ceng-xu-bian-li-by-jo-nlx3/
#参考：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/tao-mo-ban-bfs-he-dfs-du-ke-yi-jie-jue-by-fuxuemin/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #方法1：BFS+迭代
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


    #思路2：dfs+递归
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        def dfs(root,deep):
            if not root:
                return
            #res的第一层元素代表的是每层存储的val值。
            # 若deep和res长度相同，则代表当前需要空的list来存储新的val。
            if len(res)==deep:
                res.append([])

            res[deep].append(root.val)
            dfs(root.left,deep+1)
            dfs(root.right,deep+1)


        dfs(root,0)
        return res






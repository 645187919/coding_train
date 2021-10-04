#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-04 15:39 
# @Author : magician 
# @File : 199_medium.py 
# @Software: PyCharm

# 199. 二叉树的右视图
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 示例 1:
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
# 示例 2:
# 输入: [1,null,3]
# 输出: [1,3]
# 示例 3:
# 输入: []
# 输出: []
# 提示:
#
# 二叉树的节点个数的范围是 [0,100]
# -100 <= Node.val <= 100


# 参考：https://leetcode-cn.com/problems/binary-tree-right-side-view/solution/dfs-bfs-by-powcai-7/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #方法1：bfs
        if not root:
            return []
        res=[]
        queue=[root]
        while queue:
            #每次把右边节点给加进来
            res.append(queue[-1].val)
            ll=[]
            for node in queue:
                if node.left:
                    ll.append(node.left)
                if node.right:
                    ll.append(node.right)
            queue=ll
        return res


        #方法2DFS:利用res[deep]=root.val将右子树的值覆盖左子树，最终达到目标
        # res=[]
        # def helper(root,deep):
        #     if not root:
        #         return
        #     if len(res)==deep:
        #         res.append(0)
        #     #若存在右节点，则直接覆盖左节点
        #     res[deep]=root.val
        #     helper(root.left,deep+1)
        #     helper(root.right,deep+1)
        # helper(root,0)
        # return res




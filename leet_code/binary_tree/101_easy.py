#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-31 21:02 
# @Author : magician 
# @File : 101_easy.py 
# @Software: PyCharm


# 101. 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# 1
# / \
#     2   2
# / \ / \
#     3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# 1
# / \
#     2   2
# \ \
#     3    3
# 进阶：
# 你可以运用递归和迭代两种方法解决这个问题吗？

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#参考：https://leetcode-cn.com/problems/symmetric-tree/solution/101-dui-cheng-er-cha-shu-di-gui-fa-die-dai-fa-xian/
#（详细说递归的写法）

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        #递归+DFS
        #递归终止条件：若同层的对称节点的值不相等，则终止；
        #否则递归的比较同层的左右对称节点。
        def helper(left,right):
            # left/right都为空节点
            if not left and not right:
                return True
            # left/right有一个为空（全为空在上面已排除）
            elif not left or not right:
                return False
            elif left.val!=right.val:
                return False
            # 将左右子节点对称递归比较
            return helper(left.left,right.right) & helper(left.right,right.left)

        return helper(root.left,root.right)

        # 方法二：迭代算法
        # （思想：将根节点的左右节点入队列，然后依次弹出比较。之后再将根节点的孩子节点
        # 按照对称节点的位置入队列。再迭代的比较。）
        from collections import deque
        if not root:
            return True
        deq = deque([root.left,root.right])
        while deq:
            root_right = deq.pop()
            root_left = deq.pop()
            if root_left == None and root_right == None:
                continue
            if root_left == None or root_right == None:
                return False
            if root_left.val != root_right.val:
                return False
            deq.extend([root_left.left,root_right.right,root_left.right,root_right.left])
        return True
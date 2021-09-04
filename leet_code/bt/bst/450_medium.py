#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-04 14:36 
# @Author : magician 
# @File : 450_medium.py 
# @Software: PyCharm

# 450. 删除二叉搜索树中的节点
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
# 一般来说，删除节点可分为两个步骤：
# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
#
# 示例:
# root = [5,3,6,2,4,null,7]
# key = 3
#
# 5
# / \
#     3   6
# / \ \
#     2   4   7
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
#
# 5
# / \
#     4   6
# / \
#     2       7
# 另一个正确答案是 [5,2,6,null,4,null,7]。
#
# 5
# / \
#     2   6
# \ \
#     4   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # tmp=root

        # def get_min(root):
        #     if not root:
        #         return
        #     while root.left is not None:
        #         root=root.left
        #     return root.val


        # def remove(self,root,key):
        #     if not root:
        #         return None

        #     if root.val>key:
        #         #对左子树接着进行删除操作,当前节点的左子树指向删除后子树
        #         root.left=self.remove(root.left,key)
        #     elif root.val<key:
        #         root.right=self.remove(root.right,key)
        #     else:
        #         #等于key,看子树的类型
        #         if root.left is None and root.right is None:
        #             root = None
        #             return root
        #         #若只有右子树，则覆盖root节点
        #         elif not root.left:
        #             root=root.right
        #         elif not root.right:
        #             root=root.left
        #         else:
        #             #去要剔除节点的右子树中寻找最小的节点值，并进行覆盖
        #             root.val=self.get_min(root.right)
        #             #删除右子树中最小的节点值
        #             root.right=self.remove(root.right,root.val)

        #     return root


        # 思路：先查找待删除结点
        # 找到后有四种情况
        # case0 结点不存在，empty,return root
        # case1 结点没孩子,直接删除
        # case2 结点只有一个孩子,是左孩子,让左孩子即位
        # case3 结点只有一个孩子,是右孩子,让右孩子即位
        # case4 结点有俩孩子,用 right tree left most 替换待删除结点,然后把right tree left most那个结点删除
        if root is None: # case 0 要删除的节点不存在
            return root
        if root.val > key: # 要删除的结点在左子树
            root.left = self.deleteNode(root.left, key)
        elif root.val < key: # 要删除的结点在右子树
            root.right = self.deleteNode(root.right, key)
        else: # 已经找到了要删除的结点,开始进行删除操作
            # case1 没有孩子,直接删除返回空
            if root.left is None and root.right is None:
                root = None
                return root
            # case2 只有一个孩子,左孩子,让左孩子即位
            elif root.left is not None and root.right is None:
                tmp = root.left
                root = None
                return tmp
            # case3 只有一个孩子,右孩子,让右孩子即位
            elif root.right is not None and root.left is None:
                tmp = root.right
                root = None
                return tmp
            # case4 有两个孩子,和右子树 left most交换后在右子树中删除 left most
            else:
                curr = root.right # 右子树
                while curr.left: # find left most
                    curr = curr.left
                # 退出while循环时候的curr就是left most
                root.val = curr.val # 即位
                root.right = self.deleteNode(root.right, curr.val) # 在右子树中删除该结点后作为新的右子树
        return root

#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-30 22:24 
# @Author : magician 
# @File : 226.py 
# @Software: PyCharm

# 226. 翻转二叉树
# 翻转一棵二叉树。
#
# 示例：
# 输入：
# 4
# / \
#     2     7
# / \   / \
#     1   3 6   9
# 输出：
# 4
# / \
#     7     2
# / \   / \
#     9   6 3   1
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
# 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。



#思路：https://leetcode-cn.com/problems/invert-binary-tree/solution/di-gui-han-shu-zen-yao-xie-ben-wen-bang-zhu-ni-li-/
#参考：更直白的写法
# https://leetcode-cn.com/problems/invert-binary-tree/solution/dong-hua-yan-shi-liang-chong-shi-xian-226-fan-zhua/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# 最后，提醒大家避免踩一个小坑，不能直接写成下面这样的代码：
# root.left = invert(root.right)
# root.right = invert(root.left)
# 这是因为第一行修改了root.left，会影响了第二行。
# 在 Python 中，正确的写法是把两行写在同一行，就能保证 root.left 和 root.right 的修改是同时进行的。

    #方法2：迭代法bfs
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        queue=[root]
        while queue:
            ll=[]

            for node in queue:
                #互换
                node.left,node.right=node.right,node.left
                if node.left:
                    ll.append(node.left)
                if node.right:
                    ll.append(node.right)
            queue=ll
        return root







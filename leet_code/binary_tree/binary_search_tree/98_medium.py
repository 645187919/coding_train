#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-02 22:27 
# @Author : magician 
# @File : 98.py 
# @Software: PyCharm

# 98. 验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
# 输入:
# 2
# / \
#     1   3
# 输出: true
# 示例 2:
#
# 输入:
# 5
# / \
#     1   4
# / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。

#思路：https://leetcode-cn.com/problems/validate-binary-search-tree/solution/zhi-yao-san-xing-di-gui-gao-ding-python3-by-jimmy0/

def isValidBST(self, root: TreeNode, low = float('-inf'), high = float('inf')) -> bool:

    if not root:return True
    if not low<root.val<high:return False
    return self.isValidBST(root.left,low,root.val) and self.isValidBST(root.right,root.val,high)

#20211006 update
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.res=True

        #1、定义递归函数的参数(每次迭代包含一个最大和最小值的范围)和返回值（bool）。
        def helper(root,min,max):

            #2、递归终止条件
            if not root:
                return
            if root.val<=min or root.val>=max:
                self.res=False
                return
                #单层递归的逻辑：对其子树进行核验(左子树最大值限制，右子树最小值限制)
            helper(root.left,min,root.val)
            helper(root.right,root.val,max)
        helper(root,-float('inf'),float('inf'))
        return self.res
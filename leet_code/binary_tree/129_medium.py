#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-02 20:50 
# @Author : magician 
# @File : 129_medium.py 
# @Software: PyCharm

# 129. 求根节点到叶节点数字之和
# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：
# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
# 计算从根节点到叶节点生成的 所有数字之和 。
# 叶节点 是指没有子节点的节点。

# 示例 1：
# 输入：root = [1,2,3]
# 输出：25
# 解释：
# 从根到叶子节点路径 1->2 代表数字 12
# 从根到叶子节点路径 1->3 代表数字 13
# 因此，数字总和 = 12 + 13 = 25
# 示例 2：
# 输入：root = [4,9,0,5,1]
# 输出：1026
# 解释：
# 从根到叶子节点路径 4->9->5 代表数字 495
# 从根到叶子节点路径 4->9->1 代表数字 491
# 从根到叶子节点路径 4->0 代表数字 40
# 因此，数字总和 = 495 + 491 + 40 = 1026

# 提示：
# 树中节点的数目在范围 [1, 1000] 内
# 0 <= Node.val <= 9
# 树的深度不超过 10

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #简易写法：分两种情况，叶子节点和非叶子节点（即递归的终止条件）
    def sumNumbers(self, root: TreeNode) -> int:
        res=[]

        def helper(root,path):
            if not root:
                return
            #若节点不为空，则将节点加入路径记录变量中
            path+=str(root.val)
            #若是叶子节点则加入res
            if not root.left and not root.right:
                res.append(path)
            #否则，递归每个非叶子节点的左右子节点
            helper(root.left,path)
            helper(root.right,path)
        helper(root,'')
        #list求和的简便写法
        return sum([int(num) for num in res])



    # def sumNumbers(self, root: TreeNode) -> int:
    #     res=[]
    #     #记录子路径
    #     def sum_total(root,tmp_list):
    #         if not root:
    #             return
    #         print(tmp_list)
    #         if not root.left and not root.right:
    #             tmp_list+=[root.val]
    #             res.append(tmp_list)
    #
    #         sum_total(root.left,tmp_list+[root.val])
    #         sum_total(root.right,tmp_list+[root.val])
    #     sum_total(root,[])
    #     sum_res=0
    #     print(res)
    #     for i in res:
    #         #注意这里list转化为str时若str中的元素类型为int时则需要先转成str。然后再拼接
    #         num="".join(str(j) for j in i)
    #         sum_res+=int(num)
    #     return sum_res


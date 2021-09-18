#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-18 21:31 
# @Author : magician 
# @File : 77_medium.py 
# @Software: PyCharm

# 77. 组合
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。
# 示例 1：
# 输入：n = 4, k = 2
# 输出：
# [
#     [2,4],
#     [3,4],
#     [2,3],
#     [1,2],
#     [1,3],
#     [1,4],
# ]
# 示例 2：
#
# 输入：n = 1, k = 1
# 输出：[[1]]
# 提示：
# 1 <= n <= 20
# 1 <= k <= n


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res=[]
        choise_result=[]
        for i in range(1,n+1):
            choise_result.append(i)


        def helper(path,choise):

            #终止条件:当path长度等于k时
            if len(path)==k:
                res.append(path)
            #考虑选择列表要怎么构建，什么时候可以直接用选择列表的元素即i为元素；
            #什么时候用选择列表的索引，即i为索引
            for i in range(len(choise)):
                #结果集每个子序列都是升序，所以直接用choise[i+1:]
                helper(path+[choise[i]],choise[i+1:])

        helper([],choise_result)
        return res




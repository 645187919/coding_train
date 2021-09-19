#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-19 14:52 
# @Author : magician 
# @File : 216_medium.py 
# @Software: PyCharm

# 216. 组合总和 III
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        tmp_result=[]
        res=[]

        for i in range(1,10):
            #注意构造选择列表的时候，若k为2则代表2个元素，
            # 则剔除最大的元素1，若k=3则代表剔除最大元素2。以此来达到优化剪枝的目的
            if i<=n-(k-1):
                tmp_result.append(i)

        def helper(path,choise):
            total=0
            for j in path:
                total+=j

            #终止条件:path长度为k以及path大小为n
            if len(path)==k and total==n:
                res.append(path)
                return
            for i in range(len(choise)):
                helper(path+[choise[i]],choise[i+1:])

        helper([],tmp_result)
        return res









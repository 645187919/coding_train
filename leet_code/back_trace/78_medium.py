#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-19 15:43 
# @Author : magician 
# @File : 78_medium.py 
# @Software: PyCharm

# 78. 子集
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
# 提示：
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res=[]
        nums_len=len(nums)

        def helper(path,choise):
            print(path)
            print(choise)
            #终止条件：若路径小于等于nums长度，则加入然后停止
            if nums_len>=len(path) and res!=[]:
                res.append(path)
                #注意return的作用：结束当前的递归。
                # 若不加return则代表在该递归条件下接着走下面的程序，在树结构中相当于不断的向树底探索。
                #return
            else:
                res.append(path)

            for i in range(len(choise)):
                helper(path+[choise[i]],choise[i+1:])

        helper([],nums)
        return res
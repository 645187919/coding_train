#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-18 21:06 
# @Author : magician 
# @File : 47_medium.py 
# @Software: PyCharm

# 47. 全排列 II
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 示例 1：
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 示例 2：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 提示：
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        #回溯：终止条件需要调整下
        res=[]
        def helper(path,choise):
            if not choise:
                #若当前路径未在结果集中再添加
                if path not in res:
                    res.append(path)
                return

            for i in range(len(choise)):
                helper(path+[choise[i]],choise[:i]+choise[i+1:])
        helper([],nums)
        return res

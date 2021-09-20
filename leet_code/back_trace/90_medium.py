#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-19 16:01 
# @Author : magician 
# @File : 90_medium.py 
# @Software: PyCharm


# 90. 子集 II
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
#
# 示例 1：
#
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 示例 2：
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        res=[]
        nums_len=len(nums)
        #注意排下序，方便查找重复元素，避免重复操作
        nums.sort()

        def helper(path,choise):
            #无终止条件
            if nums_len>=len(path) and res!=[]:
                res.append(path)
            else:
                res.append([])

            for i in range(len(choise)):
                if choise[i]==choise[i-1] and i!=0:
                    continue
                else:
                    helper(path+[choise[i]],choise[i+1:])
        helper([],nums)
        return res


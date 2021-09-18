#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-18 20:55 
# @Author : magician 
# @File : 46_medium.py 
# @Software: PyCharm

# 46. 全排列
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 示例 1：
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：
# 输入：nums = [1]
# 输出：[[1]]
#
# 提示：
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        len_nums=len(nums)

        def helper(path,choise):
            #终止条件:当路径到达底层树的时候或者选择列表为空的时候停止
            if len(path)==len_nums:
                res.append(path)
                return
                #回溯
            #for 选择 in range(选择列表)
            for i in range(len(choise)):
                #一定要注意是题目要求是不重复的数据，也就是每次迭代的选择列表要剔除掉当前选择的节点元素！！
                helper(path+[choise[i]],choise[0:i]+choise[i+1:])

        helper([],nums)
        return res

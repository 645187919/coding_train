#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-29 22:07 
# @Author : magician 
# @File : 347.py 
# @Software: PyCharm

# 347. 前 K 个高频元素
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
# 提示：
#
# 1 <= nums.length <= 105
# k 的取值范围是 [1, 数组中不相同的元素的个数]
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #暴力法：用map存储，key为元素，val为频次.然后对val进行降序排序，获取topK的key值返回
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=dic.get(nums[i],0)+1

        new_dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(new_dic[i][0])
        return res
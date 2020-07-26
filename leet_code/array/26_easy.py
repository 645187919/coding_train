#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/26 14:37 
# @Author : magician 
# @File : 26_easy.py 
# @Software: PyCharm


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # n=len(nums)
        # # if nums is null or n==0:
        # #     return
        # s=0
        # f=1
        # while f<n:

        #     if nums[s]==nums[f]:
        #         f+=1
        #     elif nums[s]!=nums[f]:
        #         nums[s+1]=nums[f]
        #         f+=1
        #         s+=1
        # return len(nums[:s+1])




        # 方法二：快满指针，不考虑最终的数组是什么样，只考虑返回的长度
        n=len(nums)
        s=0#满指针用于保存去重的元素
        #快指针用于筛选去重的元素
        for f in range(1,n):
            if nums[s]!=nums[f]:
                #满指针腾出一个位置
                s+=1
                #将新元素放入满指针数组中。
                nums[s]=nums[f]

        return s+1







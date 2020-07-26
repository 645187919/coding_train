#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/26 15:55 
# @Author : magician 
# @File : 80_medium.py 
# @Software: PyCharm


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        n=len(nums)

        s=0
        # 添加一个flag，指示i位置是否已经达到2个重复项。
        # 如果已达到（flag=True）,无脑跳过
        # 如果未达到（flag=False）,移动i
        flag=False
        for f in range(1,n):
            if nums[s]!=nums[f]:
                #s腾出来一个位置
                s+=1
                nums[s]=nums[f]
                flag=False

            else:
                if not flag:
                    s+=1
                    nums[s]=nums[f]
                    flag=True

        return s+1






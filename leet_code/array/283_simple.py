#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/21 21:02 
# @Author : magician 
# @File : 283.py 
# @Software: PyCharm


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #方法一：快慢指针，将快指针的非零元素和慢指针元素互换位置。
        # #快慢指针解决问题，快指针遍历数组，不等于0就和慢指针交换位置。然后慢指针+1（慢指针确定一个非零元素的位置）
        # j=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         j+=1

        #方法二：快慢指针，将非零元素前移，然后填充零元素
        n=len(nums)
        j=0#在[0,j]中元素为非零元素
        for i in range(n):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        for x in range(j,n):
            nums[x]=0
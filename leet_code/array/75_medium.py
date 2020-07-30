#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/30 21:07 
# @Author : magician 
# @File : 75_medium.py 
# @Software: PyCharm


class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # #三路快排的特殊版本
        # lis=self.quick_sort_3_way(nums,0,len(nums)-1)
        # return lis

        #三指针
        cur=0
        start=0
        n=len(nums)
        end=n-1

        while cur<=end:
            if nums[cur]==0:
                #将star数组（0数组）扩大一位
                nums[cur],nums[start]=nums[start],nums[cur]

                cur+=1
                start+=1
            elif nums[cur]==2:
                #将end数组（2数组）扩大一位
                nums[cur],nums[end]=nums[end],nums[cur]
                end-=1
            else:
                cur+=1







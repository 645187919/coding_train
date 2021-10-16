#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/21 21:02 
# @Author : magician 
# @File : 283.py 
# @Software: PyCharm



#283. 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。


#思路：快慢指针解决问题，快指针遍历数组，不等于0就和慢指针交换位置。
# 然后慢指针+1（慢指针确定一个非零元素的位置）
# 只要关注慢指针对应非零数组即可！
#指针有两个作用：1、链表的指示器，

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #方法一：快慢指针，将快指针的非零元素和慢指针元素互换位置。
        # #快慢指针解决问题，快指针遍历数组，不等于0就和慢指针交换位置。然后慢指针+1（慢指针确定一个非零元素的位置）
        s=0
        n_lenth=len(nums)
        #快指针遍历数组
        for f in range(n_lenth):
            #慢指针保证非零元素的数组，所以快指针只要不为零就和满指针交换位置。然后慢指针加一
            if nums[f]!=0:
                nums[f],nums[s]=nums[s],nums[f]
                s+=1

        #方法二：快慢指针，将非零元素前移，然后填充零元素
        n=len(nums)
        j=0#在[0,j]中元素为非零元素
        for i in range(n):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        for x in range(j,n):
            nums[x]=0
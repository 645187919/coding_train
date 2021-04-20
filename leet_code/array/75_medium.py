#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/30 21:07 
# @Author : magician 
# @File : 75_medium.py 
# @Software: PyCharm

#75. 颜色分类
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，
# 并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 注意:
# 不能使用代码库中的排序函数来解决这道题。

# 示例:
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]

# 进阶：
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？

#思路：三指针（三路快排），lt,gt指针，分别控制比中间元素小和大的数组。
# 相比较于三路快排比较简单的一点是这里的元素已经给出，只有0,1，2
#所以这里直接判别每个元素是0,1,2中的哪一个然后交换到对应的数组即可。

class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # #三路快排的特殊版本
        # lis=self.quick_sort_3_way(nums,0,len(nums)-1)
        # return lis

        #三指针
        #cur指针遍历元素
        cur=0
        #小于1的数组的指标
        start=0
        n=len(nums)
        #大于1的数组的指针
        end=n-1

        while cur<=end:
            if nums[cur]==0:
                #将star数组（0数组）扩大一位
                nums[cur],nums[start]=nums[start],nums[cur]
                #cur+1是由于当前cur指针对应的值已为确认的值；
                cur+=1
                start+=1
            elif nums[cur]==2:
                #将end数组（2数组）扩大一位
                nums[cur],nums[end]=nums[end],nums[cur]
                end-=1
            else:

                cur+=1







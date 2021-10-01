#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/26 15:55 
# @Author : magician 
# @File : 80_medium.py 
# @Software: PyCharm

#80. 删除排序数组中的重复项 II
#给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1:
# 给定 nums = [1,1,1,2,2,3],
# 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
# 你不需要考虑数组中超出新长度后面的元素。

#思路：快慢指针，慢指针用于限定不重复数据的数组。快指针用于遍历数组寻找目标元素。
# 特殊点：中间需要一个flag来标识每个元素是否重复两次！(留意下！)


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
                #若元素未重复两次，满指针接着扩充。然后把flag变为True
                if not flag:
                    s+=1
                    nums[s]=nums[f]
                    flag=True

        return s+1

    #方法二：双指针：一个维护动态数组的大小，一个比较s和s+2索引的元素是否相等
    # 由于是有序的，所以只需要管局s和s+2索引的位置是否相等，若相等则剔除s+2的元素
    def removeDuplicates(self, nums: List[int]) -> int:
        s=0
        lens=len(nums)-2
        while lens>s:
            if nums[s]==nums[s+2]:
                nums.pop(s+2)
                lens-=1
            else:
                s+=1
        return len(nums)

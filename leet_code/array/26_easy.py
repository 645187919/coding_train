#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/26 14:37 
# @Author : magician 
# @File : 26_easy.py 
# @Software: PyCharm

#26. 删除排序数组中的重复项
# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 示例 1:
# 给定数组 nums = [1,1,2],
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
# 你不需要考虑数组中超出新长度后面的元素。


#思路：快慢指针，慢指针i用于保障不重复元素数组，快指针用于遍历数组寻找不重复的元素。

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
                #慢指针扩出一个位置
                s+=1
                #将新元素放入满指针数组中。
                nums[s]=nums[f]

        return s+1







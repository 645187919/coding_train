#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/6 21:08 
# @Author : magician 
# @File : 167_easy.py 
# @Software: PyCharm



# 167. 两数之和 II - 输入有序数组
# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
#
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:
#
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

#思路：对撞指针的思想（双指针）。根据有序数组，且返回两个索引，则根据两个数与targe的关系来移动索引。

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #逻辑含义：头尾指针索引。碰撞指针的思想来解决
        start=0
        end=len(numbers)-1

        #头尾指针不能交互（要返回两个值的索引）
        while start<end:
            if numbers[start]+numbers[end]==target:
                return start+1,end+1

            elif numbers[start]+numbers[end]>target:
                end-=1
            else:
                start+=1

        return False


#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-28 17:16 
# @Author : magician 
# @File : 15.py 
# @Software: PyCharm

# 15. 三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
# 输入：nums = []
# 输出：[]
# 示例 3：
# 输入：nums = [0]
# 输出：[]
# 提示：（nums的大小，直接影响是否可以使用暴力法）
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

#思路：排序+双指针

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 特判，对于数组长度 nn，如果数组为 nullnull 或者数组长度小于 33，返回 [][]。
        # 对数组进行排序。
        # 遍历排序后数组：
        # 若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 00，直接返回结果。
        # 对于重复元素：跳过，避免出现重复解
        # 令左指针L=i+1，右指针R=n−1，当L<R 时，执行循环：
        # 当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
        # 若和大于 0，说明 nums[R] 太大，R 左移
        # 若和小于 0，说明 nums[L] 太小，L 右移

        len_nums=len(nums)
        result=[]
        if len_nums<3:
            return result

        nums.sort()

        #遍历数组
        for i in range(len_nums):
            #若排序后的最小值大于0，则返回result。
            if nums[i]>0:
                return result
            #若元素重复，则跳过
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len_nums-1
            while l<r:
                #若满足条件，则将组合加入result
                if nums[i]+nums[l]+nums[r]==0:
                    result.append([nums[i],nums[l],nums[r]])
                    #判断左指针和其下一位是否相等，若相等则移动指针
                    while (l<r and nums[l]==nums[l+1]):
                        l+=1
                    while (l<r and nums[r]==nums[r-1]):
                        r-=1
                    #移动左右指针
                    l+=1
                    r-=1
                #若大于

                elif (nums[i]+nums[l]+nums[r]>0):
                    r-=1
                else:
                    l+=1
        return result




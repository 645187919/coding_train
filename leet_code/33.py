#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/23 21:38 
# @Author : magician 
# @File : 33.py 
# @Software: PyCharm


# 33. 搜索旋转排序数组
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 你可以假设数组中不存在重复的元素。
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1


#思路：突破点时间复杂度为logn 则考虑用二分查找法。

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target is None:
            return False

        #必定有一半是有序的，利用这一半有序的队列来突破
        #l,r代表每次搜索list的边界索引
        l,r=0,len(nums)-1

        #缩减到一个元素，所以需要l=r
        while l<=r:

            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            #若0-mid有序（注意边界值）
            if nums[mid]>=nums[0]:
                #若target在范围内，则更改r边界
                if nums[mid]>target>=nums[0]:
                    r=mid-1
                else:
                    l=mid+1

            else:
                if nums[mid]<target<=nums[len(nums)-1]:
                    l=mid+1
                else:
                    r=mid-1

        return -1






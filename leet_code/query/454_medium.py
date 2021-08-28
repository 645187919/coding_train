#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-28 21:18 
# @Author : magician 
# @File : 454_medium.py 
# @Software: PyCharm


# 454. 四数相加 II
# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
# 例如:
#
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# 输出:
# 2
#
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

#思路：方法一：分组 + 哈希表
# 我们可以将四个数组分成两部分，AA 和 BB 为一组，CC 和 DD 为另外一组。
# 对于 AA 和 BB，我们使用二重循环对它们进行遍历，得到所有 A[i]+B[j]A[i]+B[j] 的值并存入哈希映射中。对于哈希映射中的每个键值对，每个键表示一种 A[i]+B[j]A[i]+B[j]，对应的值为 A[i]+B[j]A[i]+B[j] 出现的次数。
# 对于 CC 和 DD，我们同样使用二重循环对它们进行遍历。当遍历到 C[k]+D[l]C[k]+D[l] 时，如果 -(C[k]+D[l])−(C[k]+D[l]) 出现在哈希映射中，那么将 -(C[k]+D[l])−(C[k]+D[l]) 对应的值累加进答案中。
# 最终即可得到满足 A[i]+B[j]+C[k]+D[l]=0A[i]+B[j]+C[k]+D[l]=0 的四元组数目。



class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        #map的存储结果决定了，适合存储类似k,v的形式，即类似key，count
        dic={}
        dic1={}
        #记录结果值
        count=0

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dic[nums2[j]+nums1[i]]=dic.get(nums2[j]+nums1[i],0)+1

        for i in range(len(nums3)):
            for j in range(len(nums4)):
                total=nums4[j]+nums3[i]
                if dic.get(-total) is not None:
                    count+=dic[-total]
        return count
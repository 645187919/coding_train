#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-11-02 21:11 
# @Author : magician 
# @File : offer_04.py 
# @Software: PyCharm

# 剑指 Offer 04. 二维数组中的查找
# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
#
# 示例:
# 现有矩阵 matrix 如下：
# [
#     [1,   4,  7, 11, 15],
#     [2,   5,  8, 12, 19],
#     [3,   6,  9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。
#
# 限制：
# 0 <= n <= 1000
# 0 <= m <= 1000

#两个有序的数组
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        if m==0:
            return False
        n=len(matrix[0])
        if n==0:
            return False

        for i in range(m):
            if matrix[i][-1]<target:
                continue
            for j in range(n):
                if matrix[i][j]==target:
                    return True

        return False


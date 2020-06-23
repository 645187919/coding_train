#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/23 21:02 
# @Author : magician 
# @File : 16.07.py 
# @Software: PyCharm

# 面试题 16.07. 最大数值
# 编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。
#
# 示例：
#
# 输入： a = 1, b = 2
# 输出： 2

#解题思路：https://leetcode-cn.com/problems/maximum-lcci/solution/li-yong-shu-xue-si-wei-de-fang-fa-by-nhan/

class Solution:
    def maximum(self, a: int, b: int) -> int:
        #求两个数最大值的数学公式
        return (a+b+abs(a-b))/2
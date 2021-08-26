#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-26 21:24 
# @Author : magician 
# @File : 202_easy.py 
# @Software: PyCharm


# 编写一个算法来判断一个数 n 是不是快乐数。
# 「快乐数」定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为  1，那么这个数就是快乐数。
# 如果 n 是快乐数就返回 true ；不是，则返回 false 。
# 示例 1：
# 输入：19
# 输出：true
# 解释：
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 示例 2：
# 输入：n = 2
# 输出：false
#
# 提示：
# 1 <= n <= 231 - 1

#思路：利用set来记录每次快乐值的结果，若出现循环则认为不是快乐数
#参考：https://leetcode-cn.com/problems/happy-number/solution/ha-xi-huo-zhe-kuai-man-pao-by-powcai/
class Solution:
    def isHappy(self, n: int) -> bool:
        tmp_set=set()

        while 1:
            #可以将数字转化为字符串，然后计算每位数字的平方和
            n=sum(int(i)**2 for i in str(n))
            print(n)

            if n==1:
                return True
            elif n in tmp_set:
                return False
            tmp_set.add(n)




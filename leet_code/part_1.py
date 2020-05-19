#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/5/19 16:24 
# @Author : magician 
# @File : part_1.py 
# @Software: PyCharm

# 面试题 05.04. 下一个数
# 下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。
#
# 示例1:
#
# 输入：num = 2（或者0b10）
# 输出：[4, 1] 或者（[0b100, 0b1]）
# 示例2:
#
# 输入：num = 1
# 输出：[2, -1]
# 提示:
#
# num的范围在[1, 2147483647]之间；
# 如果找不到前一个或者后一个满足条件的正数，那么输出 -1。



# solution
class Solution(object):
    def findClosedNumbers(self,num):
        """
        #输入num是否在范围内，若不在则转化为固定的值，若在则先转化为2进制数，然后从右往左找到最靠左边的01，然后换位为10，之后将后面所有的0移到1前面；
        略小值：从左往右找到最靠近右边的10.然后换位为01，之后将所有的1移到0前面。
        :type num: int
        :rtype: List[int]
        """
        bigger_one=lower_one = bin(num)[2:]
        bigger_one="0"+bigger_one
        last01 = bigger_one.rfind("01")
        count0 = bigger_one.count("0", last01 + 1)
        len1=len(bigger_one)-count0-last01-2
        bigger_one=bigger_one[:last01]+"10"+"0"*count0+"1"*len1

        last10 = lower_one.rfind("10")
        if last10==-1:
            lower_one = '-1'
        else:
            count1 = lower_one.count("1", last10 + 1)
            len0=len(lower_one)-count1-last10-2
            lower_one=lower_one[:last10]+"01"+"1"*count1+"0"*len0
        return [int(bigger_one,2),int(lower_one,2)]
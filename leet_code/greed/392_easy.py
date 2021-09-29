#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-29 21:39 
# @Author : magician 
# @File : 392.py 
# @Software: PyCharm

# 392. 判断子序列
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 进阶：
#
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
#
#
# 示例 1：
#
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
# 示例 2：
#
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
#
#
# 提示：
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# 两个字符串都只由小写字符组成。

#双指针
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        #双指针

        if len(s)==0:
            return True
        t_len=len(t)

        s_index=0
        t_index=0
        count=0
        for i in range(t_len):
            #若字符相同
            if s[s_index]==t[t_index]:
                s_index+=1
                t_index+=1
                count+=1
            else:
                t_index+=1
            if count==len(s):
                return True
        print(count)
        return False



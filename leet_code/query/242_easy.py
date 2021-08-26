#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-26 20:52 
# @Author : magician 
# @File : 242.py 
# @Software: PyCharm

# 242. 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
#
# 提示:
#
# 1 <= s.length, t.length <= 5 * 104
# s 和 t 仅包含小写字母

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #利用map来存储一个字符串，用另一个map存储另一个字符串，然后比较两个map是否key相同且val相同
        map_1={}
        map_2={}
        for i in s:
            if map_1.get(i) is None:
                map_1[i]=1
            else:
                map_1[i]+=1
        for j in t:
            if map_2.get(j) is None:
                map_2[j]=1
            else:
                map_2[j]+=1

        if len(map_1)!=len(map_2):
            return False
        else:
            for x in map_1.items():
                #key不同
                if map_2.get(x[0]) is None:
                    return False
                #val不同
                elif map_2.get(x[0])!=x[1]:
                    print(map_2.get(x[0]))
                    print(x[1])
                    return False
            return True


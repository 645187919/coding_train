#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-26 22:13 
# @Author : magician 
# @File : 290_easy.py 
# @Software: PyCharm

# 290. 单词规律
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 示例 2:
#
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 示例 3:
#
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 示例 4:
#
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。

#思路：用map来存储，key存储pattern，val存储str，之后遍历map，看相同的key下对应的val是否也相同

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #用map来存储，key存储pattern，val存储str，之后遍历map，看相同的key下对应的val是否也相同

        map_1={}
        lens=len(pattern)
        s_arr=s.split(" ")

        if len(set(pattern))!=len(set(s_arr)):
            return False
        elif len(pattern)!=len(s_arr):
            return False

        for i in range(lens):
            #若key不存在，且对应的val值不在map中。则存入map
            if (map_1.get(pattern[i]) is None) and (s_arr[i] not in map_1.values()):
                map_1[pattern[i]]=s_arr[i]
            elif (map_1.get(pattern[i]) is None) and (s_arr[i] in map_1.values()):
                return False
            #若map中存在key,则看下val值是否相同
            elif map_1[pattern[i]]!=s_arr[i]:
                return False

        return True









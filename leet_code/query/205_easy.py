#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-28 16:27 
# @Author : magician 
# @File : 205_easy.py 
# @Software: PyCharm


# 205. 同构字符串
# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
#
# 示例 1:
# 输入：s = "egg", t = "add"
# 输出：true
# 示例 2：
# 输入：s = "foo", t = "bar"
# 输出：false
# 示例 3：
# 输入：s = "paper", t = "title"
# 输出：true
#
# 提示：
# 可以假设 s 和 t 长度相同。


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #用dict来存储s和t，若dict中不存在则存入，若存在则判断val值是否相同，若相同，则存入，否则返回false，遍历完成则返回True

        dic={}

        for i in range(len(s)):
            print(s[i])
            print(t[i])
            #若key不存在，且val也不存在，才能加入dict
            if dic.get(s[i]) is None and t[i] not in dic.values():
                dic[s[i]]=t[i]
            #若key不存在但是对应的val已经存在，则返回false
            elif dic.get(s[i]) is None and t[i] in dic.values():
                return False
            #若key存在，但是对应val值不同，则返回false
            elif dic.get(s[i]) is not None and dic[s[i]]!=t[i]:
                return False

        return True

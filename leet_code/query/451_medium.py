#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-02 15:21 
# @Author : magician 
# @File : 451_medium.py 
# @Software: PyCharm

# 451. 根据字符出现频率排序
# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
#
# 示例 1:
# 输入:
# "tree"
# 输出:
# "eert"
#
# 解释:
# 'e'出现两次，'r'和't'都只出现一次。
# 因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
# 示例 2:
# 输入:
# "cccaaa"
# 输出:
# "cccaaa"
# 解释:
# 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
# 注意"cacaca"是不正确的，因为相同的字母必须放在一起。
# 示例 3:
#
# 输入:
# "Aabb"
# 输出:
# "bbAa"
#
# 解释:
# 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
# 注意'A'和'a'被认为是两种不同的字符。

#注意：1、如何将dict按照values排序；2、dict向tuple或list的转化；3、sorted内置方法的使用。

class Solution:
    def frequencySort(self, s: str) -> str:

        dic={}

        for i in s:
            dic[i]=dic.get(i,0)+1
        #由于map无法解决数据顺序性的问题，所以将map转化为其他数据结构处理
        set_res=[(key,val) for key,val in dic.items()]
        #利用sorted在set或list中对dict中的元素，按照val排序
        sort_res=sorted(set_res,key=lambda x:x[1],reverse=True)
        final_res="".join([item[0]*int(item[1]) for item in sort_res])
        return final_res
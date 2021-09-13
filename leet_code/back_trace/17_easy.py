#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-13 21:35 
# @Author : magician 
# @File : 17_easy.py 
# @Software: PyCharm

# 17. 电话号码的字母组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 示例 1：
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 示例 2：
# 输入：digits = ""
# 输出：[]
# 示例 3：
# 输入：digits = "2"
# 输出：["a","b","c"]
#
#
# 提示：
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。

#思路：排列组合就是回溯。
#回溯的模板

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        conversion={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        digits_len=len(digits)
        res=[]
        if digits=='':
            return []

        def back_track(path,nextdigit):
            """

            :param path:路径（即树结构对应的已走过的路）
            :param nextdigit:选择列表（即要走的路）
            :return:
            """
            #回溯的终止条件:当路径长度和输入长度一致时停止递归。
            if  len(path)==digits_len:
                res.append(path)
                return
            #for 选择 in 选择列表（这里即每个按键对应的字母）
            for word in conversion[nextdigit[0]]:
                #做选择（即决策树对应决策路径）
                path+=word
                #我们定义的 backtrack 函数其实就像⼀个指针，在这棵树上游⾛，
                # 同时要正确维护每个节点的属性，每当⾛到树的底层，其「路径」就是⼀个全排列
                #下一个层
                back_track(path,nextdigit[1:])
                #撤销选择
                path=path[:-1]

        back_track('',digits)
        return res







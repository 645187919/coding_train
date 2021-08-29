#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-07-04 16:59 
# @Author : magician 
# @File : 20_easy.py 
# @Software: PyCharm

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#  
# 示例 1：
# 输入：s = "()"
# 输出：true
# 示例 2：
# 输入：s = "()[]{}"
# 输出：true
# 示例 3：
# 输入：s = "(]"
# 输出：false
# 示例 4：
# 输入：s = "([)]"
# 输出：false
# 示例 5：
# 输入：s = "{[]}"
# 输出：true
# 提示：
# 1 <= s.length <= 104
# s 仅由括号 '()[]{}' 组成


#思路：利用栈的对称性来解决括号对称的问题；

class Solution:
    def isValid(self, s: str) -> bool:

        #声明一个栈用来存放左括号
        stack=[]

        if len(s)<=1:
            return False

        #遍历s
        for i in s:
            #若为左括号则压入栈
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            #为右括号,则判断栈顶元素和当前右括号是否匹配。
            else:
                #若s中只包含右括号数据
                if len(stack)==0:
                    return False
                elif i==")" and stack[-1]=="(":
                    stack.pop(-1)
                elif i=="}" and stack[-1]=="{":
                    stack.pop(-1)
                elif i=="]" and stack[-1]=="[":
                    stack.pop(-1)
                else:
                    return False
        #当s遍历完且stack被清空时，才代表s符合要求
        return  True if len(stack)==0 else False






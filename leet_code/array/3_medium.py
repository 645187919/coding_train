#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/9 17:53 
# @Author : magician 
# @File : 3_medium.py 
# @Software: PyCharm


# 3. 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


#思路：双指针滑动窗口思想


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #滑动窗口的思想
        max_length=0
        n=len(s)
        #不重复的子串
        substr=[]
        #子串长度
        cur_length=0
        for right in range(n):
            #子串包含重复元素的话，先剔除子串首位重复元素，再将后面“重复”的元素加进来
            if substr.__contains__(s[right]):
                # 获取其在窗口中的位置
                index = substr.index(s[right])
                #截取不重复的子串
                substr=substr[index+1:]
                #将“重复”元素加进来
                substr.append(s[right])
                #更新子串长度
                cur_length=len(substr)

            else:
                #添加到子串
                substr.append(s[right])
                #子串长度加1
                cur_length+=1

            #每移动一下指针判断下最大长度
            if cur_length>max_length:
                max_length=cur_length

        return max_length
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-14 21:28 
# @Author : magician 
# @File : 131.py 
# @Software: PyCharm



# 131. 分割回文串
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 回文串 是正着读和反着读都一样的字符串。
#
# 示例 1：
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 示例 2：
#
# 输入：s = "a"
# 输出：[["a"]]
#
#
# 提示：
# 1 <= s.length <= 16
# s 仅由小写英文字母组成

#思路：回溯
#参考：https://leetcode-cn.com/problems/palindrome-partitioning/solution/dong-tai-gui-hua-dfs-by-powcai/
#https://leetcode-cn.com/problems/palindrome-partitioning/solution/131-fen-ge-hui-wen-chuan-hui-su-sou-suo-yp2jq/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(s, tmp):
            #回溯的终止条件（即到达树底时的情况）本题指s待探索区域为空
            if not s:
                res.append(tmp)
            #由于判断s中每个子串是否为回文，所以需要分别查看s长度为1,2,3...n时对应的子串的情况
            #for 选择 in 选择列表（子串的长度）
            for i in range(1, len(s) + 1):
                #若子串为回文串,则对剩余子串进行回溯。
                if s[:i] == s[:i][::-1]:
                    #把子串添加到路径中
                    #对剩余子串进行回溯
                    #Python 解法在每次搜索位置区域的时候，使用的是产生一个新数组 path + [s[:i]] ，
                    #这样好处是方便：不同的路径使用的是不同的 path，因此不需要 path.pop() 操作；
                    #而且 res.append(path) 的时候不用深度拷贝一遍 path。
                    #######即 helper(s[i:], tmp+[s[:i]])等效于
                    #tmp=tmp+[s[:i]]
                    #helper(s[i:], tmp)
                    #tmp.pop()
                    helper(s[i:], tmp+[s[:i]])
        helper(s, [])
        return res

#20211006 update

    def partition(self, s: str) -> List[List[str]]:

        len_s=len(s)
        res = []
        #确定回溯函数的参数及返回值
        def helper(path,choise):
            #终止条件：若path的长度等于s总长度
            tmp="".join(path)
            # print(len(tmp))
            if len(tmp)==len_s:
                res.append(path)
                return

            for i in range(1,len(choise)+1):
                #若是回文串，则对剩余字符串进行递归:注意如何将一个列表反转
                if choise[:i]==choise[:i][::-1]:
                    helper(path+[choise[:i]],choise[i:])
        helper([],s)
        return res
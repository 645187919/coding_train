#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-27 21:46 
# @Author : magician 
# @File : 474_medium.py 
# @Software: PyCharm

# 474. 一和零
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 请你找出并返回 strs 的最大子集的长度，该子集中最多 有 m 个 0 和 n 个 1 。
# 如果 x 的所有元素也是 y 的元素，集合x是集合y的子集 。
# 示例 1：
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
# 示例 2：
#
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
# 提示：
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] 仅由 '0' 和 '1' 组成
# 1 <= m, n <= 100

#详情参考代码随想录

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #dp[i][j]:给定m和n时对应的最大子集的长度
        #递推公式：dp[i][j]=max(dp[i][j],dp[i-numzeres][j-numones]+1) 即numzeres和numones代表的是一个元素的0和1的个数。
        #初始化：
        dp=[[0]*(n+1) for i in range(m+1)]
        #遍历
        for str in strs:
            numzeres=str.count('0')
            numones=str.count('1')

            for i in range(m,numzeres-1,-1):
                for j in range(n,numones-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-numzeres][j-numones]+1)

        return dp[m][n]

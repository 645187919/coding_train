#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-26 20:50 
# @Author : magician 
# @File : 91_medium.py 
# @Software: PyCharm

# 91. 解码方法
# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
# 题目数据保证答案肯定是一个 32 位 的整数。
# 示例 1：
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2：
#
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 示例 3：
#
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
# 示例 4：
#
# 输入：s = "06"
# 输出：0
# 解释："06" 不能映射到 "F" ，因为字符串含有前导 0（"6" 和 "06" 在映射中并不等价）。
# 提示：
#
# 1 <= s.length <= 100
# s 只包含数字，并且可能包含前导零。

#参考：https://leetcode-cn.com/problems/decode-ways/solution/gong-shui-san-xie-gen-ju-shu-ju-fan-wei-ug3dd/


class Solution:
    def numDecodings(self, s: str) -> int:


        #dp[i]：长度为i的字符对应的解码方法的总数

        #递推公式：若第i位可以单独解码则dp[i]+=dp[i-1]
        #若第i位和第i-1位合起来可以解码则dp[i]+=dp[i-2]
        #总的解码总数等于

        #初始化dp[0]=1
        #遍历
        len_s=len(s)
        #dp[0]不做处理
        dp=[0 for i in range(len_s+1)]
        dp[0]=1

        for i in range(1,len_s+1):
            #若i的前一位不为0则i和i-1对应的解码总数相等
            if int(s[i-1])!=0:
                dp[i]+=dp[i-1]
            #若i的前两位在10-26之间则i和i-2对应的解码总数相等
            if 26>=int(s[i-2])*10+int(s[i-1])>=10 and i>1:
                dp[i]+=dp[i-2]
        print(dp)
        return dp[-1]


# 参考：https://leetcode-cn.com/problems/decode-ways/solution/c-wo-ren-wei-hen-jian-dan-zhi-guan-de-jie-fa-by-pr/

class Solution:
    def numDecodings(self, s: str) -> int:

        if s.startswith('0'):
            return 0
        n=len(s)
        if n<=1:
            if s[0]!='0':
                return 1
            else:
                return 0

        #dp[i]:长度为i+1的字符串的解码总数
        dp=[0 for i in range(n+1)]

        dp[0]=1;dp[-1]=1
        for i in range(1,len(s)):
            # '0'只有10和20才有对应字母，不然 返回 0
            if s[i]=='0':
                if s[i-1]=='1' or s[i-1]=='2':
                    dp[i] = dp[i-2]
                else:
                    return 0
            # 看分析，如果是 10~26，则 dp[i] = dp[i-1] + dp[i-2]，否则 编码数目不变，仍然为 dp[i-1]
            else:
                if 10<int(s[i-1:i+1])<27:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp [i-1]
        # 由于dp最后一位初始化为 1，所以返回 dp的倒数第二个
        return dp[-2]


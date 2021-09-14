#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-14 21:52 
# @Author : magician 
# @File : 93_medium.py 
# @Software: PyCharm

# 93. 复原 IP 地址
# 给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

# 示例 1：
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 示例 2
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 示例 3：
# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 示例 4：
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
# 示例 5：
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# 提示：
# 0 <= s.length <= 3000
# s 仅由数字组成


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        r = []
        def restore(count=0, ip='', s=''):
            # count record split times, ip record ip, s record remaining string
            #记录终止条件
            if count==4:
                if s=='':
                    r.append(ip[:-1])
                return

            #几种选择
            if len(s)>0:
                #回溯
                restore(count+1,ip+s[0]+'.',s[1:])
                #ip每个子单元长度大于1且首字母不为0
            if len(s)>1 and s[0]!='0':
                restore(count+1,ip+s[:2]+'.',s[2:])
            if len(s)>2 and s[0]!='0' and int(s[0:3])<256:
                restore(count+1,ip+s[:3]+'.',s[3:])
        restore(0,'',s)
        return r



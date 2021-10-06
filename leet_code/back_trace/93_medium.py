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

# 参考：https://leetcode-cn.com/problems/restore-ip-addresses/solution/python3-hui-su-suan-fa-bao-li-sou-suo-ji-1hzx/
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #结果存储函数
        result = []
        #当前路径
        path = []
        #回溯函数
        def back_track(s, index):
            #减枝，如果搜索路径大于4，直接返回
            if len(path) > 4:
                return
                #全部搜素完成，搜索路径等于4，则加入结果列表
            if index == len(s) and len(path) == 4:
                result.append(".".join(path))
                return
            #遍历整个字符串，对每一个满足的子串递归回溯
            for i in range(index, len(s)):
                #减枝，如果当前值在0-255之前，则开始回溯
                if 0 <= int(s[index : i+ 1]) <= 255:
                    #如果当前值是0，但是不是一个单"0"则剪掉
                    if int(s[index : i+ 1]) == 0 and i != index:
                        continue
                    #如果当前值不是0，但是缺以"0XXX"开头，也应该剪掉
                    if int(s[index : i+ 1]) > 0 and s[index] == "0":
                        continue
                    #加入当前path
                    path.append(s[index: i+ 1])
                    #从当前节点开始递归
                    back_track(s, i + 1)
                    #回溯
                    path.pop()
        back_track(s, 0)
        return result




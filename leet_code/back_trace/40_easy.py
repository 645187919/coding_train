#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-18 22:43 
# @Author : magician 
# @File : 40_easy.py 
# @Software: PyCharm

# 40. 组合总和 II
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次。
# 注意：解集不能包含重复的组合。
#
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
#     [1,1,6],
#     [1,2,5],
#     [1,7],
#     [2,6]
# ]
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
#     [1,2,2],
#     [5]
# ]
#
# 提示:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #注意特殊情况
        #数组长度等于0.等于1的情况
        if len(candidates)==0:
            return candidates
        if len(candidates)==1:
            if candidates[0]!=target:
                return []
            else:
                return [candidates]

        res=[]
        #注意
        #先对candidates进行排序，直接剔除大于目标值的数据。
        #注意list的操作如何实现如排序，计算和，统计每个元素的个数等
        candidates.sort()
        index_flag=len(candidates)
        for i in range(len(candidates)):
            if candidates[i]>target:
                index_flag=i
                break
        candidates=candidates[0:index_flag]


        def helper(path,choise):
            #终止条件:等于target的话，就加进来。大于的话就停止
            total=0

            for i in path:
                total+=i

            if total==target:
                res.append(path)
                return

            if total>target:
                return

            for i in range(len(choise)):
                #注意是否为list的首位，若不为首位，且相邻元素相等，则不需要对后一个元素再做回溯处理，
                # 因为得到的结果和前一个元素相同，只会增加重复元素。
                if i!=0 and choise[i]==choise[i-1]:
                    continue
                #由于对输入的choise路径进行了排序，且每个元素只让使用依次，则直接用choise[i+1:]。
                helper(path+[choise[i]],choise[i+1:])

        helper([],candidates)
        return res
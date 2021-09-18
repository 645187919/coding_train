#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-18 21:53 
# @Author : magician 
# @File : 39_medium.py 
# @Software: PyCharm

# 39. 组合总和
# 给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。
# candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。
# 对于给定的输入，保证和为 target 的唯一组合数少于 150 个。
# 示例 1：
# 输入: candidates = [2,3,6,7], target = 7
# 输出: [[7],[2,2,3]]
# 示例 2：
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
# 示例 3：
# 输入: candidates = [2], target = 1
# 输出: []
# 示例 4：
# 输入: candidates = [1], target = 1
# 输出: [[1]]
# 示例 5：
# 输入: candidates = [1], target = 2
# 输出: [[1,1]]
#
# 提示：
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都是独一无二的。
# 1 <= target <= 500

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(path,choise):

            #终止条件：path的和等于target添加到res，若大于target则停止
            total=0
            for i in path:
                total+=i
            if total==target:
                res.append(path)
                return
            if total>target:
                return

            for i in range(len(choise)):
                #注意题目中输入为升序所以每次递归就选择choise[i:]，这样就避免了元素相同顺序不同的“相同组合”题目规定
                helper(path+[choise[i]],choise[i:])
        helper([],candidates)
        return res

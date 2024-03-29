#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-20 15:29 
# @Author : magician 
# @File : 79_medium.py 
# @Software: PyCharm

# 79. 单词搜索（同类型的题：200，130）
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
# 如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，
# 其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。
# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# 输出：true
# 示例 3：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# 输出：false
#
# 提示：
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board 和 word 仅由大小写英文字母组成

#思路:回溯。采用的还是回溯的模板，只不过情况更加复杂，做了些许改动。
#首先对于矩阵中的每个节点都要进行回溯的检测，即树结构的第一层就是所有的矩阵节点值。
#其次对矩阵每个节点进行回溯的时候，要判断清楚回溯的终止条件：如果不匹配则终止，如果全匹配也终止；
#否则不断的迭代；
#最终在对每个匹配的节点进行上下左右探索的时候，为了避免往回探索，需要将走过的‘路’做标记，
# 即将以匹配的节点设置为特征状态，探索结束后再复原！

#参考：https://leetcode-cn.com/problems/word-search/solution/79dan-ci-sou-suo-li-jie-liang-ge-xiao-ke-rh6b/

class Solution:

    def exist(self, board, word):
        #思路：dfs+回溯（每个节点选择路径的回溯）
        row, col = len(board), len(board[0])

        def dfs(x, y, index):
            """
            x,y：矩阵的索引；（理解为路径path）
            index：待匹配的目标字符串的索引（理解为选择列表choise）
            """
            #回溯的终止条件：
            #1、若当前的矩阵元素不等于目标字符串word的字符，则结束当前矩阵字符的回溯，跳入下一字符。
            if board[x][y] != word[index]:
                return False
            #2、若匹配到目标字符串的word最后一个字符，则代表满足最终条件
            if index == len(word) - 1:
                return True
            #匹配的坐标先被标记为已匹配（防止后续再反过来搜索），再对其周围的坐标进行匹配。
            board[x][y] = '#'
            #代表当前元素和word字符匹配的情况下，再去探索四周的元素。
            #即 for 选择 in 选择列表：
            for choice in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                #做出选择
                nx, ny = x + choice[0], y + choice[1]
                #到树结构的下一个节点
                if 0 <= nx < row and 0 <= ny < col and dfs(nx, ny, index + 1):
                    return True
            #若周围的坐标没有匹配，则复原匹配的坐标。
            board[x][y] = word[index]

        #提前多了一层循环，需要对每个节点都进行回溯！
        for i in range(row):
            for j in range(col):
                #每个节点选择路径的回溯
                if dfs(i, j, 0):
                    return True
        return False



#方法二：基于回溯终止条件，for 选择 in 选择列表 这样的模板的实现。

class Solution:

    def exist(self, board, word):
        #思路：dfs+回溯（每个节点选择路径的回溯）
        row, col = len(board), len(board[0])

        def dfs(x, y, index):
            """
            x,y：矩阵的索引；（理解为路径path）
            index：待匹配的目标字符串的索引（理解为选择列表choise）
            """
            #回溯的终止条件：首先判断坐标索引是否符合规范。不规范则停止树的生长（探索）
            if not(0 <= x < row) or not (0 <= y < col):
                return False
            #其次判断节点值是否和目标值匹配，若不匹配则返回False。
            if board[x][y] != word[index]:
                return False
            #若匹配到目标字符串的word最后一个字符，则代表满足最终条件
            if index == len(word) - 1:
                return True
            #匹配的坐标先被标记为已匹配（防止后续再反过来搜索），再对其周围的坐标进行匹配。
            board[x][y] = '#'
            #代表当前元素和word字符匹配的情况下，再去探索四周的元素。
            #即 for 选择 in 选择列表：
            for choice in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                #也是将方法内部True和False值向外部传递的一种方法吧。
                #探索树结构的下一个节点，若满足最终的条件则返回True，否则则一直的DFS遍历节点。
                if dfs(x + choice[0],  y + choice[1], index + 1):
                    return True

            #若周围的坐标没有匹配，则复原匹配的坐标。
            board[x][y] = word[index]

        for i in range(row):
            for j in range(col):
                #每个节点选择路径的回溯
                if dfs(i, j, 0):
                    return True
        return False
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-20 19:21 
# @Author : magician 
# @File : 130_meidum.py 
# @Software: PyCharm

# 130. 被围绕的区域
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，
# 并将这些区域里所有的 'O' 用 'X' 填充。
# 示例 1：
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 示例 2：
#
# 输入：board = [["X"]]
# 输出：[["X"]]
#
#
# 提示：
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] 为 'X' 或 'O'

# 思路：
# 那么，我们只要找到四周边界上存在O且与这些O连接着的O，在搜索时先修改成其他字母，比如“#”。
# 然后遍历二维矩阵，将为O修改为X，将#修改为O即可

# 参考：https://leetcode-cn.com/problems/surrounded-regions/solution/pythonshen-du-you-xian-sou-suo-jiang-jie-xi-zhi-zh/
# 参考:https://leetcode-cn.com/problems/surrounded-regions/solution/yuan-di-xiu-gai-de-dfs-python130-bei-wei-rao-de-qu/
class Solution:
    def solve(self, board):
        row, col = len(board), len(board[0])

        def dfs(x, y):
            #回溯的终止条件：不为O则终止当前的树的生成。
            if board[x][y] != 'O':
                return
            #若为0则转化为其他字符
            else:
                board[x][y] = '#'
            for c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= x + c[0] < row and 0 <= y + c[1] < col:
                    dfs(x + c[0], y + c[1])
        #先对首列和末列做操作即将边界的O和其相邻的O转化为其他字符
        for i in range(row):
            #知道遍历的操作（直接执行某方法）和判断的操作（需要外部的if条件等）
            dfs(i, 0)
            dfs(i, col - 1)
        ##对首行和末行的其他元素操作(注意这个n_row-1是开口即不包含该列)
        for j in range(1, col - 1):
            dfs(0, j)
            dfs(row - 1, j)
        ##将剩余的内部的O转化为X
        for i in range(row):
            for j in range(col):
                board[i][j] = 'O' if board[i][j] == '#' else 'X'
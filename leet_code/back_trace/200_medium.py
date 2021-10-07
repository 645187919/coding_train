#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-20 16:17 
# @Author : magician 
# @File : 200_medium.py 
# @Software: PyCharm

# 200. 岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
#
# 示例 1：
# 输入：grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]
# 输出：1
# 示例 2：
# 输入：grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# 输出：3

# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'

#回溯的终止条件：1、明确的定义return；
# 2、无终止条件即不做任何声明，即会遍历到当前节点下，树的最底层。

#思路：针对这道题，我们只需要对矩阵进行依次遍历，如果当前grid[x][y] == "1",则启动DFS模式。
# 找到与之相连的所有1，将其置为0。搜索结束后，我们找到了一个岛屿，岛屿数量+=1。
# 如此循环，最终返回岛屿数量即可

#同类型的题（79,130）
# 参考：https://leetcode-cn.com/problems/number-of-islands/solution/200dao-yu-shu-liang-ju-zhen-sou-suo-top3-ww71/

# 二维平面上的DFS模板：https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n_rows=len(grid)
        n_col=len(grid[0])
        count=0

        def helper(x,y):
            """
            这里由于选择列表是固定的，所以只传路径参数
            :param x:
            :param y:
            :return:
            """
            #终止条件：当坐标不在规定范围内或节点值不为1，则终止
            if not (0<=x<n_rows) or not (0<=y<n_col) or grid[x][y]!='1':
                return

            #将探索过满足条件的岛屿区域都置为0做标记。
            grid[x][y]='0'
            #基于当前节点做回溯探索
            for choise in [[0,-1],[0,1],[-1,0],[1,0]]:
                xn=x+choise[0]
                yn=y+choise[1]
                helper(xn,yn)

        for i in range(n_rows):
            for j in range(n_col):
                if grid[i][j]=='1':
                    helper(i,j)
                    count+=1
        return count
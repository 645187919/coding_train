#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-20 16:17 
# @Author : magician 
# @File : 200_medium.py 
# @Software: PyCharm



#回溯的终止条件：1、明确的定义return；
# 2、无终止条件即不做任何声明，即会遍历到当前节点下，树的最底层。

#思路：针对这道题，我们只需要对矩阵进行依次遍历，如果当前grid[x][y] == "1",则启动DFS模式。
# 找到与之相连的所有1，将其置为0。搜索结束后，我们找到了一个岛屿，岛屿数量+=1。
# 如此循环，最终返回岛屿数量即可


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
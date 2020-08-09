#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/9 16:02 
# @Author : magician 
# @File : 11_medium.py 
# @Software: PyCharm

# 11. 盛最多水的容器
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

# 示例：
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49

#思路：对撞指针思想：抓住向内移动短板，面积可能会更大的要点。


class Solution:

    def maxArea(self, height: List[int]) -> int:

        #对撞指针思想：抓住向内移动短板，面积可能会更大的要点。

        n=len(height)

        if n==2:
            return height[1]*1 if height[0]>height[1] else height[0]*1

        start=0
        end=n-1
        #初始头尾指针组成的面积
        max_val= height[end]*end if height[start]>height[end] else height[start]*end
        while start<end:

            #比较两边
            if height[start]<height[end]:
                #移动短边
                start+=1
                longe=end-start
                wide=height[end] if height[start]>height[end] else height[start]
                #求新的面积
                new_area=longe*wide
                #若新面积大则替换
                if new_area>max_val:
                    max_val=new_area

            else:
                #移动短边
                end-=1
                longe=end-start
                wide=height[end] if height[start]>height[end] else height[start]
                #求新的面积
                new_area=longe*wide
                #若新面积大则替换
                if new_area>max_val:
                    max_val=new_area

        return max_val

#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/12 16:11 
# @Author : magician 
# @File : __init__.py.py 
# @Software: PyCharm

'''
heaqp模块提供了堆队列算法的实现，也称为优先级队列算法。
要创建堆，请使用初始化为[]的列表，或者可以通过函数heapify（）将填充列表转换为堆。
提供以下功能：
heapq.heappush（堆，项目）
将值项推入堆中，保持堆不变。
heapq.heapify（x）
在线性时间内将列表x转换为堆。
heapq.heappop（堆）
弹出并返回堆中的最小项，保持堆不变。如果堆是空的，则引发IndexError。
'''
import heapq

#1 heappush生成堆+ heappop把堆从小到大pop出来
heap = []
data = [1,3,5,7,9,2,4,6,8,0]
for i in data:
    heapq.heappush(heap,i)
print(heap)

lis = []
while heap:
    lis.append(heapq.heappop(heap))
print(lis)

#2 heapify生成堆+ heappop把堆从小到大pop出来
data2 = [1,5,3,2,9,5]
heapq.heapify(data2)
print(data2)

lis2 = []
while data2:
    lis2.append(heapq.heappop(data2))
print(lis2)




import heapq

# 第一种
"""
函数定义：
heapq.heappush(heap, item)
    - Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap)
    - Pop and return the smallest item from the heap, maintaining the heap invariant.
    If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
"""
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)  # 加入堆

print(heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]


# 第二种
nums = [2, 3, 5, 1, 54, 23, 132]
# print(nums.index())
print(nums.)
heapq.heapify(nums)
print([heapq.heappop(nums) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]

#输出结果
# [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 5, 9, 5]
# [1, 2, 3, 5, 5, 9]


s="abcabcbb"
for i in s:
    print(i)
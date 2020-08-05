#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/5 22:00 
# @Author : magician 
# @File : 215_medium.py 
# @Software: PyCharm

# 215. 数组中的第K个最大元素
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

#思路：堆排序，快排改进版（只去找前K个值）

def max_heapify(heap, heapSize, root):
    """
    对传入的数据进行最大堆化
    :param heap:
    :param heap_size:
    :param i:
    :return:
    """
    left = 2*root + 1
    right = left + 1
    larger = root

    #先更换索引
    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right

    if larger!=root:
        #最后更换位置
        heap[larger],heap[root]=heap[root],heap[larger]
        #递归的对子树接着进行最大堆化（自底向上构建，每上一层（相对的顺序会被打乱重新排序），都要对下面的“子树”进行重新的堆化处理。
        max_heapify(heap,heapSize,larger)



def build_max_heap(heap):
    """
    自下而上创建一个大顶堆
    :param heap:
    :return:
    """
    heapSize = len(heap)
    for i in range((heapSize -2)//2,-1,-1):
        # heapSize -2代表该索引节点一定有父节点，(heapSize -2)//2代表有多少个根节点
        #从下到上依次对各个root子树进行排序。
        max_heapify(heap, heapSize, i)



def heap_sort(heap):
    build_max_heap(heap)
    #上一步构建最大堆已经确定了一个最大元素即堆顶元素
    #将堆首最大元素和末尾元素互换，这样不断的减小待排序的数据队列
    for i in range(len(heap)-1,-1,-1):
        #更换堆顶元素和堆尾元素（扩充已排序的数组）
        heap[0],heap[i]=heap[i],heap[0]
        #对未排序的数组再选出最大的堆顶元素添加到已排序的数组中
        max_heapify(heap,i,0)
if __name__ == '__main__':
    a = [57,50,30,77,62,78,94, 80, 84]

    print(a)
    heap_sort(a)
    print(a)
    b=[3,1,2,4]
    heap_sort(b)
    print(b)
    print(b[-2])
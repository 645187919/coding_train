#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/4 20:44 
# @Author : magician 
# @File : heap_sort.py 
# @Software: PyCharm





import random

def max_heapify(heap,heapSize,root):  # 调整列表中的元素并保证以root为根的堆是一个大根堆
    """

    :param heap: 输入的堆
    :param heapSize: 对应要操作的堆的大小
    :param root: 相应的根节点
    :return:
    给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
    父节点：(root-1)//2
    左子节点：2*root + 1
    右子节点：2*root + 2  即：左子节点 + 1
    """
    left = 2*root + 1
    right = left + 1
    larger = root


    #对该root根节点子树进行排序。若叶子节点小于根节点，则先更换索引
    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right
    #更换相应的叶子节点和根节点的val
    if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作
        heap[larger], heap[root] = heap[root], heap[larger]
        #递归的对子树接着进行最大堆化（自底向上构建，每上一层（相对的顺序会被打乱重新排序），都要对下面的“子树”进行重新的堆化处理。
        max_heapify(heap, heapSize, larger)


def build_max_heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    heapSize = len(heap)
    for i in range((heapSize -2)//2,-1,-1):  # 自底向上建堆。
        # heapSize -2代表该索引节点一定有父节点，(heapSize -2)//2代表有多少个根节点
        #从下到上依次对各个root子树进行排序。
        max_heapify(heap, heapSize, i)
def heap_sort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行堆调整过程。
    build_max_heap(heap)
    #上一步构建最大堆已经确定了一个最大元素即堆顶元素
    #将堆首最大元素和末尾元素互换，这样不断的减小待排序的数据队列
    for i in range(len(heap)-1,-1,-1):
        #更换堆顶元素和堆尾元素（扩充已排序的数组）
        heap[0],heap[i]=heap[i],heap[0]
        #对未排序的数组再选出最大的堆顶元素添加到已排序的数组中
        max_heapify(heap,i,0)


# 测试
if __name__ == '__main__':
    a = [57,50,30,77,62,78,94, 80, 84]
    print(a)
    heap_sort(a)
    print(a)
    # b = [random.randint(1,1000) for i in range(1000)]
    # print(b)
    # heap_sort(b)
    # print(b)

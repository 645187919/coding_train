#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/15 21:04 
# @Author : magician 
# @File : 61_medium.py 
# @Software: PyCharm


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #声明特殊情况
        if head is None or k==0:return head
        """ 迭代 - 将倒数第k个元素作为新的头，再将原来的头链接到原来的尾上 """
        # 1: 获取长度，且原头尾连接成环
        count=1
        cur=head
        while cur.next is not None:
            count+=1
            cur=cur.next
        #闭环
        cur.next=head
        # 2: 原尾部节点指针游走 length - k % length 步, 到达新的尾部节点
        t=count-k%count
        while t:
            cur=cur.next
            t-=1
        # 3: 新的尾部与头部节点断开连接，返回新的头部节点
        head=cur.next
        cur.next=None
        return head








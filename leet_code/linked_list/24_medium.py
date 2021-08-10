#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/9/10 21:21 
# @Author : magician 
# @File : 24_medium.py 
# @Software: PyCharm
# 24. 两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：
#
# 输入：head = []
# 输出：[]
# 示例 3：
#
# 输入：head = [1]
# 输出：[1]


#解法一：利用指针的特性，更改相邻两个节点间的指向
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dumy_head=ListNode(-1)
        #虚拟节点指向head
        dumy_head.next=head
        print(id(dumy_head))
        #生成一个pre指针。pre指向dummy_head节点
        pre=dumy_head
        print(id(pre))
        print(pre.next)
        while pre.next and pre.next.next:
            #（生成a,b两个指针）
            a,b=pre.next,pre.next.next
            #a节点指向b之后的节点
            a.next=b.next
            #前置指针指向b
            pre.next=b
            #b指向a
            b.next=a
            #移动pre
            pre=pre.next.next
        #     pre=cur.next
        #     cur=cur.next.next
        #     cur.next=cur

        return dumy_head.next
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/9/10 21:21 
# @Author : magician 
# @File : 24_medium.py 
# @Software: PyCharm


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
        #生成一个pre指针（实质也就是一个节点）。pre指向dummy_head
        pre=dumy_head
        print(id(pre))
        print(pre.next)
        while pre.next and pre.next.next:
            #（生成a,b两个节点）
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
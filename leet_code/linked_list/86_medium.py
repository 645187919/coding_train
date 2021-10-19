#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/25 21:23 
# @Author : magician 
# @File : 86_medium.py 
# @Software: PyCharm

# 86. 分隔链表
# 给定一个链表和一个特定值x，对链表进行分隔，使得所有小于x的节点都在大于或等于x的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5


#思路：创建两个链表用于分别存储大于和小于等于的target的数据。
#遍历所有的链表，然后再把两个链表链接起来。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        #创建两个空链表
        dummy_head=ListNode(-1)
        dummy_head_1=ListNode(-2)
        #创建对应的指针（两个作用：1、串联链表；2、控制链表大小）
        p1,p2=dummy_head,dummy_head_1
        #头结点指针
        cur=head
        while cur:
            if cur.val<x:
                #添加cur指针对应的节点到链表
                p1.next=cur
                #移动p1指针
                p1=p1.next

            else:
                p2.next=cur
                p2=p2.next
            #遍历原始链表的下一个元素
            cur=cur.next
        #连接两个链表
        p1.next=dummy_head_1.next
        #另一个链表p2置为None
        p2.next=None
        return dummy_head.next


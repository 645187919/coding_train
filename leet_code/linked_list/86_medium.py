#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/25 21:23 
# @Author : magician 
# @File : 86_medium.py 
# @Software: PyCharm

# 86. 分隔链表
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5


#思路：用两个链表分别存储两边的数据，然后将两个链表链接

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dumy_head_1=ListNode(-1)
        dumy_head_2=ListNode(-1)
        p1=dumy_head_1
        p2=dumy_head_2
        while head:
            if head.val<x:
                p1.next=head
                #移动p1，扩充链表大小
                p1=p1.next
            else:
                p2.next=head
                p2=p2.next
            #移动head
            head=head.next

        # 连接两个链表
        p1.next=dumy_head_2.next #dumy_head2一直没有改变
        p2.next=None
        return dumy_head_1.next


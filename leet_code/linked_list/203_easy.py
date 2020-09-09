#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/9/1 20:37 
# @Author : magician 
# @File : 203_easy.py 
# @Software: PyCharm

# 203. 移除链表元素
# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# 思路：创建一个虚拟头结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        #创建虚拟节点用作标记新链表头部
        dumy_head=ListNode(-1)
        dumy_head.next=head
        #创建对应的指针
        #prev=ListNode(-1)
        prev=dumy_head
        while (prev.next!=None):
            if prev.next.val==val:
                prev.next=prev.next.next

            else:
                prev=prev.next
        return  dumy_head.next




#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/15 14:45 
# @Author : magician 
# @File : 206_easy.py 
# @Software: PyCharm

# 206. 反转链表
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

#思路：双指针。需要一个 cur 指针表示当前遍历到的节点；一个 pre 指针表示当前节点的前驱节点；
# 在循环中还需要一个中间变量 temp 来保存当前节点的后驱节点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #反转指针的操作
        #思路：双指针。dummy_heat,cur指针
        pre=None
        cur=head

        while cur:
            #先保存cur的next节点，防止丢失。
            tmp=cur.next
            #cur指针指向反面
            cur.next=pre
            #pre向前移.顺序不能乱
            pre=cur
            #cur向前移
            cur=tmp
        return pre
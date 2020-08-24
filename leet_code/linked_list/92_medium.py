#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/24 21:01 
# @Author : magician 
# @File : 92_medium.py 
# @Software: PyCharm

# 92. 反转链表 II
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

#思路：先找到需要反转的链表，然后利用双指针反转，参考206。最后把反转后的链表和原链表进行连接

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        #移动到需要移动的链表处
        dummy = ListNode(-1)
        dummy.next = head
        a, d = dummy, dummy
        for _ in range(m - 1):
            a = a.next
        for _ in range(n):
            d = d.next
        #通过双指针反转链表
        b, c = a.next, d.next
        pre = b
        cur = pre.next
        while cur != c:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        #将反转后的链表和原始链表链接
        a.next = d
        b.next = c
        return dummy.next



#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-03 17:10 
# @Author : magician 
# @File : 445_medium.py 
# @Software: PyCharm

# 445. 两数相加 II
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。
# 将这两数相加会返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#示例1：
# 输入：l1 = [7,2,4,3], l2 = [5,6,4]
# 输出：[7,8,0,7]
# 示例2：
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[8,0,7]
# 示例3：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
# 提示：
#
# 链表的长度范围为 [1, 100]
# 0 <= node.val <= 9
# 输入数据保证链表代表的数字无前导 0

#思路：先反转链表，再参考leetcode2将两个数相加，然后再反转链表

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def reverseList(head: ListNode) -> ListNode:
            pre=None
            cur=head
            while cur:
                #保存next节点
                tmp=cur.next
                #反转指向
                cur.next=pre
                #移动两个指针
                pre=cur
                cur=tmp
            return pre
        revers_l1=reverseList(l1)
        revers_l2=reverseList(l2)
        l3=ListNode(0)
        p3=l3
        p1,p2=revers_l1,revers_l2
        carry=0
        while p1 or p2:
            x=  p1.val  if p1 else 0
            y=  p2.val  if p2 else 0
            total=x+y+carry
            carry=total//10
            result=total%10
            p3.next=ListNode(result)
            p3=p3.next
            if p1:
                p1=p1.next
            if p2:
                p2=p2.next
        if carry!=0:
            p3.next=ListNode(carry)
        revers_l3=reverseList(l3.next)

        return revers_l3

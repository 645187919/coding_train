#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/27 21:08 
# @Author : magician 
# @File : 2_medium.py 
# @Software: PyCharm

# 2. 两数相加
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


#标准版本
# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)  #头结点，无存储，指向链表第一个结点
        node = head         #初始化链表头结点指针
        carry = 0           #初始化 进一 的数
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry              # 对每一位求和
            carry = sum // 10                # 地板除，求进一（其为0或1）
            #先有next对应的节点，才能有后续的移动
            node.next = ListNode(sum % 10)   # 取余数，求本位结点
            if l1:                           # 求空否，防止出现无后继结点
                l1 = l1.next
            if l2:                           # 同上
                l2 = l2.next
            node = node.next                 # 更新指针
        if carry != 0:                       # 验证最后一位相加是否需 进一
            node.next = ListNode(1)
        return head.next                     # 返回头结点的下一个结点，即链表的第一个结点




#20210816：自己实现的版本：
# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #创建结果链表
        head=ListNode(0)
        #链表头指针
        cur=head
        #进位标志
        count=0
        #当l1或l2存在的时候就进行运算
        while l1 or l2:
            #具体判断l1和l2的情况：
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            sums=x+y+count #两位相加的和（记得进位符）
            save_num=sums%10 #运算后每个节点保存的值
            count=sums//10 #重新对进位标识进行赋值
            #创建需要保存的节点，存储结果链表的头指针指向该节点
            # （链表：实质只要有一个头结点（存储单元）和头指针（类似于针）后续就能去指向任何节点（穿针引线））
            cur.next=ListNode(save_num)
            cur=cur.next
            #移动两个链表
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

            #最后一位若相加后进位的情况
        if count==1:
            #创建一个新的节点val为1，进行连接
            cur.next=ListNode(1)
        return head.next











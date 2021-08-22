#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/9/9 21:12 
# @Author : magician 
# @File : 21_easy.py 
# @Software: PyCharm



# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#

# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

#思路：将两个链表合并成一个链表。
#注意点：要清楚链表的基本元素设置的目的：
# 如:
# 1、怎么创建一个链表（一个节点就可以扩展成链表）
# 2、虚拟节点的作用（虚拟节点一般是为了记录链表的初始位置而声明的）
# 3、pre，cur指针声明的目的：cur指针是为了改变原链表（将原链表的线重新传引）。pre指针一般适用于双指针思想！
# 4、指针真实的意义是为了串联链表，另一层作用是控制链表的大小!
# 5、删除节点的操作：需要一个pre指针（你需要删除节点的前一个节点指向该节点的后一个节点。
# 有前驱指针就对应的需要虚拟头结点，这样才能“前驱”）。
# 6、双指针思想的应用（当需要利用的链表相邻的关系时，自然而然就要用到双指针 如82题：删除重复的全部元素）



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #dummy_head本身就是一个节点，一个节点也就意味着可以扩张为一个链表。所以本题
        #可以直接利用dummy_head来转化为合并链表。
        dummy=ListNode(-1)
        #创建两个cur指针，分别指向l1,l2
        cur1,cur2=l1,l2
        #为合并链表创建指针
        cur=dummy
        while cur1 and cur2:
            if cur1.val>=cur2.val:
                cur.next=cur2
                #cur2移位
                cur2=cur2.next
            else:
                cur.next=cur1
                #cur1移位
                cur1=cur1.next
            #扩充合并链表（cur只是虚拟节点的指针，虚拟节点要想扩充需要连接足够多的节点，就需要移动cur指针）
            #指针的另一个作用：控制链表的大小
            cur=cur.next

        if cur1:
            cur.next=cur1
        else:
            cur.next=cur2
        return dummy.next
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/26 20:39 
# @Author : magician 
# @File : 328_medium.py 
# @Software: PyCharm


# 328. 奇偶链表
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:
#
# 输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
# 说明:
#
# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

#思路：创建两个链表分别存储奇数节点和偶数节点。然后将两个链表相连。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #创建两个虚拟节点是为了找到链表的初始节点
        dumy_head=ListNode(-1)
        dumy_head_2=ListNode(-1)

        p1=dumy_head
        p2=dumy_head_2
        cur=head
        count=1

        while cur:
            num=count%2
            print(count)
            if num==1:
                #串联节点
                p1.next=cur
                #添加了一个元素，自然要移动p1，扩充链表（控制链表）。
                p1=p1.next
            else:
                p2.next=cur
                p2=p2.next
            #移动cur
            cur=cur.next
            #增加索引值
            count+=1
        #连接两个链表
        p1.next=dumy_head_2.next
        #另一个链表末尾置空
        p2.next=None
        return dumy_head.next



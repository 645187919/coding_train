#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/9/8 21:26 
# @Author : magician 
# @File : 82_medium.py 
# @Software: PyCharm

# 82. 删除排序链表中的重复元素 II
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
#思路：双指针，pre,cur。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dumy_head=ListNode(-1)
        dumy_head.next=head
        pre,cur=dumy_head,head

        while cur and cur.next:

            if cur.val==cur.next.val:
                #当相邻元素重复且有cur.next时，不断移动cur指针
                while cur.next and cur.val==cur.next.val:
                    cur=cur.next
                #此时cur依旧在相同元素的坐标下。需要指向cur.next
                pre.next=cur.next
                #移动cur
                cur=cur.next
            else:
                #移动两个指针
                pre=pre.next
                cur=cur.next

        return dumy_head.next


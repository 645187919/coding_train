#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-17 21:54 
# @Author : magician 
# @File : 148_medium.py 
# @Software: PyCharm


# 148. 排序链表
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
# 进阶：
# 你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
#
#
# 示例 1：
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
# 示例 2：
#
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
# 示例 3：
#
# 输入：head = []
# 输出：[]
#
# 提示：
#
# 链表中节点的数目在范围 [0, 5 * 104] 内
# -105 <= Node.val <= 105

#思路：转化为list排序在生成新的链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis=[]
        cur=head
        while cur:
            lis.append(cur.val)
            cur=cur.next

        lis.sort()
        print(lis)
        dummy_head=ListNode(-1)
        pre=dummy_head

        for i in range(len(lis)):
            pre.next=ListNode(lis[i])
            pre=pre.next

        return dummy_head.next




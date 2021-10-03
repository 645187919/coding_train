#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/24 21:17 
# @Author : magician 
# @File : 83_easy.py 
# @Software: PyCharm

# 83. 删除排序链表中的重复元素
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素只出现一次 。
# 返回同样按升序排列的结果链表。
# 示例 1：
# 输入：head = [1,1,2]
# 输出：[1,2]
# 示例 2：
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
#
# 提示：
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序排列

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #遍历整个链表，查看相邻的节点数值是否相等，若相等，则剔除重复的一个元素。否则移到下一个节点.
        #注意head代表的是头结点，所以不能直接拿head操作。这样就代表你的链表的头结点在移动。
        #需要一个引用来操作
        node=head
        #注意这里的限制条件，必须node及node.next同时存在
        while node and node.next:
            if node.val==node.next.val:
                node.next=node.next.next
            else:
                node=node.next

        return head
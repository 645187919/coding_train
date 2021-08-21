#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-21 15:52 
# @Author : magician 
# @File : 234_easy.py 
# @Software: PyCharm

# 234. 回文链表
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
#
# 示例 1：
# 输入：head = [1,2,2,1]
# 输出：true
# 示例 2：
# 输入：head = [1,2]
# 输出：false

#思路1：将链表数据转化为数组，然后利用双指针，从数组坐标和右边同时判断是否为回文。


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur=ListNode(-1)
        cur.next=head
        tmp_list=[]

        while cur.next:
            tmp_list.append(cur.next.val)
            cur=cur.next

        s=0
        n_len=len(tmp_list)-1
        while s<=n_len:
            if tmp_list[s]!=tmp_list[n_len]:
                return False
            s+=1
            n_len-=1
        return True

#思路2：利用堆栈，将链表每个元素压入堆栈，然后利用双指针的思想，从头和尾依次比较链表每个元素的大小。
#详情参考：https://leetcode-cn.com/problems/palindrome-linked-list/solution/hui-wen-lian-biao-de-san-chong-fang-fa-by-coldme-2/
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack=[]
        p,p2=head,head
        while p:
            stack.append(p)
            p=p.next

        while p2:
            tmp_p=stack.pop()
            if p2.val!=tmp_p.val:
                return False
            p2=p2.next
        return True




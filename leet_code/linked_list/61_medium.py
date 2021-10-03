#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/15 21:04 
# @Author : magician 
# @File : 61_medium.py 
# @Software: PyCharm


# 61. 旋转链表
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# 示例 1：
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
# 示例 2：
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
# 提示：
#
# 链表中节点的数目在范围 [0, 500] 内
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#方法二：
# 参考：https://leetcode-cn.com/problems/rotate-list/solution/fu-xue-ming-zhu-wen-ti-chai-fen-fen-xian-z4dr/
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next: return head
        # 求链表长度
        _len = 0
        cur = head
        while cur:
            _len += 1
            cur = cur.next
        # 对长度取模
        k %= _len
        if k == 0: return head
        # 让 fast 先向后走 k 步
        fast, slow = head, head
        while k:
            fast = fast.next
            k -= 1
        # 此时 slow 和 fast 之间的距离是 k；fast 指向第 k+1 个节点
        # 当 fast.next 为空时，fast 指向链表最后一个节点，slow 指向倒数第 k + 1 个节点
        while fast.next:
            fast = fast.next
            slow = slow.next
        # newHead 是倒数第 k 个节点，即新链表的头
        newHead = slow.next
        # 让倒数第 k + 1 个节点 和 倒数第 k 个节点断开
        slow.next = None
        # 让最后一个节点指向原始链表的头
        fast.next = head
        return newHead


"""
方法一：
1: 迭代 - 将倒数第k个元素作为新的头，再将原来的头链接到原来的尾上
循环找到链表长度n和链表尾，然后算一下k/n的余数，把链表连成环，
然后从尾部开始往前走n-k步，在这里断开这个环，然后返回头指针
"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #声明特殊情况
        if head is None or k==0:return head
        """ 迭代 - 将倒数第k个元素作为新的头，再将原来的头链接到原来的尾上 """
        # 1: 获取长度，且原头尾连接成环
        count=1
        cur=head
        while cur.next is not None:
            count+=1
            cur=cur.next
        #闭环
        cur.next=head
        # 2: 原尾部节点指针游走 length - k % length 步, 到达新的尾部节点
        t=count-k%count
        while t:
            cur=cur.next
            t-=1
        # 3: 新的尾部与头部节点断开连接，返回新的头部节点
        head=cur.next
        cur.next=None
        return head








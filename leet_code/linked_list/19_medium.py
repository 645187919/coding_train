#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-03 21:09 
# @Author : magician 
# @File : 19_medium.py 
# @Software: PyCharm

# 19. 删除链表的倒数第 N 个结点
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 进阶：你能尝试使用一趟扫描实现吗？
#
# 示例 1：
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#
# 提示：
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

#思路：先获取链表长度，然后找到节点删除。

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #也可以直接操作head，但是如果这样做，就无法找到链表的头节点。也就无法再表示该链表；
        #所以这里才用cur=head。用cur引用head。或者说cur为head的指针
        dummy=ListNode(-1)
        pre=dummy
        cur=head
        count=0
        while cur:
            count+=1
            #移动cur
            cur=cur.next

        pre.next=head
        num=1
        while pre.next:

            #倒数第n即正数第count-n+1
            if num==count-n+1:
                pre.next=pre.next.next
                #剔除后即结束
                break
            pre=pre.next
            num+=1

        return dummy.next
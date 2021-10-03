#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/8/15 14:44 
# @Author : magician 
# @File : __init__.py.py 
# @Software: PyCharm
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
l3=ListNode(-1)
#赋值（引用或者称为p3为l3的指针）
p3=l3
print(l3.val)
print(p3.val)
#更改p3的属性
p3.val=4
print(l3.val)
print(p3.val)
#p3指向一个新节点
p3.next=ListNode(2)
print(l3.val)
print(p3.val)
#移动过去
p3=p3.next
print(l3.val)
print(p3.val)

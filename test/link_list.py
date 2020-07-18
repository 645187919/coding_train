#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/14 20:11 
# @Author : magician 
# @File : link_list.py 
# @Software: PyCharm
#重点关注下，加强下练习！！
class node(object):
    def __init__(self,val=None,next=None):
        self.data=val
        self.next=next


class link_list(object):
    def __init__(self):
        #声明一个假的头指针(这样就不用对头结点进行特殊处理。每个节点都有指针指向)
        self.dummy_head=node()
        self.size=0

    def add(self,val,index):
        # if index>self.size:
        #     raise IndexError("index illegal")
        #链表如何查找元素，通过next属性
        pre = node()
        #pre指针的初始位置（在虚拟头结点的位置）
        pre =self.dummy_head
        #一步一步往前进，知道要添加节点的索引处
        for i in range(index):
            pre=pre.next
        #node(val,pre.next)代表一个指向pre.next的节点A。
        #pre.next=node(val,pre.next)代表pre.next指向节点A
        pre.next=node(val,pre.next)
        self.size+=1

        return pre.next.data
    def add_last(self,val):
        return self.add(val,self.size)

    def add_first(self,val):
        return self.add(val,0)

    def show_link_list(self):
        tmp_lis=[]
        pre=self.dummy_head
        for i in range(self.size):
            tmp_lis.append(pre.next.data)
            pre=pre.next

        return tmp_lis

    def remove(self,index):
        # pre=node()
        pre=self.dummy_head
        # print(id(pre))
        # print(id(self.dummy_head))
        for i in range(index):
            pre=pre.next
        #指针直接跳过删除的元素即可
        pre.next=pre.next.next
        self.size-=1

        # print(self.dummy_head.data)

    def remove_last(self):
        self.remove(self.size-1)
    def remove_first(self):
        self.remove(0)

    def set(self,val,index):
        if index>self.size:
            raise IndexError("index illegal")

        pre=self.dummy_head
        for i in range(index):
            pre=pre.next
            print(pre.data)
            print(type(pre.next))

        pre.next.data=val
        return pre.next.data

    def get(self,index):
        if index>self.size:
            raise IndexError("index illegal")
        pre=self.dummy_head
        for i in range(index):
            pre=pre.next
        return pre.next.data

    def contais(self,val):

        pre=self.dummy_head
        for i in range(self.size):

            pre=pre.next
            if pre.data==val:
                return True
            continue
        return False




ll = link_list()
for i in range(5):
    print(ll.add(i, i))
    # print(ll)
print(ll.add_first(1))
print(ll.add_last(1))
print(ll.show_link_list())
print(ll.remove(1))
print(ll.show_link_list())
print(ll.remove_last())
print(ll.remove_first())
print(ll.show_link_list())
# print(ll.dummy_head.data)
print(ll.set(6, 3))
print(ll.show_link_list())
print(ll.get(3))
print(ll.contais(2))
print(ll.contais(5))
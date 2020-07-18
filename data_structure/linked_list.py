#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/21 14:29
# @Author : magician
# @File : linked_list.py
# @Software: PyCharm


class Node(object):
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linked_list(object):
    def __init__(self):
        #初始化虚拟头节点dummmy_head
        self.dummy_head=Node()
        self.size=0
        # self.prev=Node

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size==0



    def add(self,index,value):
        """
        添加元素：使用虚拟头结点dummy_head，就不用考虑头结点这种特殊情况
        :param index:
        :param value:
        :return:
        """
        if index<0 or index>self.size:
            raise IndexError("index over")

        #声明pre指针
        prev=self.dummy_head
        #index实质也就是添加了一个虚拟头结点所以不需要减1
        #pre移动：pre=pre.next.下面的操作实质也就是移动到index的前一个节点处
        for i in range(index):
            prev=prev.next
        #插入节点操作：Node(value,prev.next)创建一个指向pre.next的节点，prev.next=Node（）指的是prev.next指向Node。
        prev.next = Node(value, prev.next)
        self.size+=1

        return prev.next.data

    def add_first(self,value):
        return self.add(0,value)

    def add_last(self,value):
        return self.add(self.size,value)



    def get(self,index):
        if index<0 or index>=self.size:
            raise IndexError("index over")
        #cur代表包含第一个元素的节点
        cur = self.dummy_head.next

        for i in range(index):
            cur = cur.next
            # print(cur.data)
        return cur.data

    def get_first(self):
        return  self.get(0)

    def get_last(self):
        return self.get((self.size)-1)#索引，需要-1

    def set(self,index,value):
        if index<0 or index>=self.size:
            raise IndexError("index over")
        cur = self.dummy_head.next

        for i in range(index):
            cur=cur.next

        cur.data=value
        return cur.data

    def contains(self,value):

        cur = self.dummy_head.next
        for i in range(self.size):
            if cur.data==value:
                return True
            cur=cur.next
        return False


    def show(self):

        cur=self.dummy_head.next
        tmp_lis=[]
        while cur != None:
            tmp_lis.append(cur.data)
            cur=cur.next

        return tmp_lis

    def to_string(self):

        cur=self.dummy_head.next
        string="None"
        while cur!=None:
            string+=("->"+str(cur.data))
            cur=cur.next

        return string

    def remove(self,index):
        """
        删除节点
        :param index:
        :return:
        """
        if index<0 or index>=self.size:
            raise IndexError("index over")

        prev=self.dummy_head
        #移动索引
        for i in range(index):
            prev=prev.next

        #删除节点的指针操作（指针跳过要删除的节点即可）
        prev.next=prev.next.next
        self.size-=1


    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self.size-1)


    def remove_element(self,value):
        prev = self.dummy_head.next
        print(type(prev))

        #终止条件：查找到链表的结尾。
        while(prev.next!=None):
            if prev.next.data==value:

                #判断pre.next是否为最后一个元素，若是需要特殊处理。
                if prev.next.next!=None:
                    print(prev.next.data)
                    prev.next=prev.next.next
                #尾部，将尾结点指向None，然后break。
                else:
                    prev.next=None
                    break
                self.size-=1
            prev=prev.next



if __name__ == '__main__':

    ll = Linked_list()
    for i in range(5):
        print(ll.add(i, i))
        # print(ll)
    print("*"*10)
    print(ll.get_size())
    print(ll.get(4))
    print(ll.get_first())
    print("*"*10)
    print(ll.get_size())
    print("*"*10)

    print(ll.get_last())
    print(ll.get_size())
    print(ll.get(2))
    print(ll.set(2, 99))
    print(ll.get(2))
    print(ll.contains(1))
    print(ll.show())
    print(ll.to_string())
    print(ll.remove(2))
    print(ll.show())
    print(ll.remove_first())
    print(ll.remove_last())
    # print(ll.remove_element(3))
    print(ll.show())
    # ll.add_last(2)
    print(ll.remove_element(3))
    print(ll.show())



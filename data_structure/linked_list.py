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
        self.dummy_head=Node()
        self.size=0
        # self.prev=Node

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size==0



    def add(self,index,value):
        """
        使用虚拟头结点，就不用考虑头结点这种特殊情况
        :param index:
        :param value:
        :return:
        """
        if index<0 or index>self.size:
            raise IndexError("index over")
        # # if (index==0):
        # #     self.add_first(value)
        # else:
        #     # node = Node
        #     prev = Node()
        #     prev=self.head
        #     for i in range(index-1):
        #         prev=prev.next
        #     prev.next = Node(value, prev.next)
        #     self.size+=1
        # # return
        # if (index==0):
        #     self.add_first(value)

        prev = Node()
        prev=self.dummy_head
        #index实质也就是添加了一个虚拟头结点所以不需要减1
        for i in range(index):
            prev=prev.next
        prev.next = Node(value, prev.next)
        self.size+=1

        return prev.next.data
    # return

    def add_first(self,value):
        # node = Node(value)
        # node.next = self.head
        # self.head=node

        # self.head = Node(value, self.head)
        # self.size+=1

        return self.add(0,value)
    def add_last(self,value):
        return self.add(self.size,value)




    def get(self,index):
        if index<0 or index>=self.size:
            raise IndexError("index over")

        cur = Node()
        #cur代表包含第一个元素的节点
        cur = self.dummy_head.next
        # print(cur.data)

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
        cur = Node()
        cur = self.dummy_head.next

        for i in range(index):
            cur=cur.next

        cur.data=value
        return cur.data

    def contains(self,value):

        cur=Node()
        cur = self.dummy_head.next
        for i in range(self.size):
            if cur.data==value:
                return True
            cur=cur.next
        return False

        # while cur!=None:
        #     if cur.data==value:
        #         return True
        #     cur=cur.next
        # return False


    def show(self):

        cur=self.dummy_head.next
        tmp_lis=[]
        while cur != None:
            # for j in range(i):
            # for j in range(i):
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
        if index<0 or index>=self.size:
            raise IndexError("index over")

        prev = Node()
        #考虑删除首节点
        prev=self.dummy_head

        for i in range(index):
            prev=prev.next

        ret_node=Node()
        ret_node=prev.next
        prev.next=ret_node.next
        ret_node.next=None
        self.size-=1

        return ret_node.data


    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self.size-1)




# # create three single nodes
# node1 = Node(15)
# node2 = Node(8.2)
# node3 = Node("Berlin")
# node4 = Node(15)
#
# track = Linked_list()
# print("track length: %i" % track.get_size())
#
# for current_node in [node1, node2, node3, node4]:
#     track.add(0,current_node)
#     print("track length: %i" % track.get_size())
#     # track.output_list()
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



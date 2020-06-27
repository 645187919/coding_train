#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/27 13:48 
# @Author : magician 
# @File : linked_list_map.py 
# @Software: PyCharm

from data_structure.linked_list import Linked_list


class Node(object):
    def __init__(self,key=-1,val=-1,next=None):
        self.key=key
        self.val=val
        self.next=next

class Linked_list_map(Linked_list):

    def __init__(self):
        self.dummy_head = Node()
        self.size=0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def get_node(self,key):
        
        cur = self.dummy_head.next
        while cur!=None:
            if cur.key==key:
                return cur
            else:
                cur = cur.next
        return None
    def contains(self,key):
        return self.get_node(key)!=None

    def get(self,key):
        node = self.get_node(key)
        return None if node==None else node.val
    def add(self,key,val):
        node = self.get_node(key)
        if node == None:
            self.dummy_head.next = Node(key, val, self.dummy_head.next)
            self.size+=1
        else:
            node.val=val

    def set(self,key,val):
        node = self.get_node(key)
        if node ==None:
            raise Exception("%s doesn't exits"%key)
        node.val=val

    def remove(self,key):
        prev = self.dummy_head
        while prev.next!=None:
            if prev.next.key == key:
                break

            prev=prev.next
        if prev.next!=None:
            del_node=prev.next
            prev.next=del_node.next
            del_node.next=None
            self.size-=1
            return del_node.val

        return None



if __name__ == '__main__':

    map = Linked_list_map()
    for i in range(7):
        map.add(i,i)

    print(map.get_size())

    print(map.get(1))

    print(map.remove(2))

    print(map.get_size())

    print(map.contains(2))

    print(map.set(4, 7))

    print(map.get(4))

    print(map.get_node(5).val)

    s = set()
    s.c


















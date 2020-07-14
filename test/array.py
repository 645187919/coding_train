#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/12 16:11 
# @Author : magician 
# @File : array.py 
# @Software: PyCharm


class array(object):
    # __size=0

    def __init__(self):
        self.data=list()
        self.size=0
        # for i in range(len):
        #     self.data.append(fillval)
        #     self.size+=1

    #考虑添加数据在数组中间的情况
    def add(self,index,val):
        self.data.append(1)#扩充一位
        #索引异常
        if index is None or index>len(self.data)-2:
            raise IndexError("index illegal")
        #数据添加在数组中间的情况
        for i in range(len(self.data)-1,-1,-1):
            #一步一步的移动元素，腾出index索引的位置
            if i>index:
                self.data[i]=self.data[i-1]
            else:
                break
        self.data[index]=val

        self.size+=1
        return self.data
    def add_last(self,val):
        self.data.append(val)
        self.size+=1
        return self.data
    def add_first(self,val):
        self.add(0,val)
        return self.data

    def get_size(self):
        return self.size

    def remove(self,index):
        # tmp_lis = self.data[index + 1:]
        self.data.pop(index)
        self.size-=1
        return self.data

    def remove_last(self):
        return self.remove(self.size-1)

    def remove_first(self):
        return self.remove(0)

    def set(self,index,val):
        self.data[index]=val
        return self.data
    def get(self,index):
        if index is None or index>self.size-1:
            raise IndexError("index illegal")

        return self.data[index]

    def contains(self,val):

        for v in self.data:
            if v==val:
                return True

        return False

    def find(self,val):
        for i in range(self.size):
            if self.data[i]==val:
                return i

        return -1

if __name__ == '__main__':
    a = array()
    print(a)
    print(a.get_size())
    for i in range(10):
        # print(a.data[i])
        print(a.add_last(i))
    print(a.get_size())
    print(a.add_first(2))
    print(a.add(2, 2))
    print(a.remove(2))
    print(a.get_size())
    print(a.remove_first())
    print(a.remove_last())
    print(a.set(2, 3))
    print(a.get(3))
    print(a.contains(10))
    print(a.contains(5))
    print(a.find(2))

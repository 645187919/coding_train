#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/27 15:05 
# @Author : magician 
# @File : max_heap.py 
# @Software: PyCharm


class array(object):

    def __init__(self,capacity=32):
        self.size=0
        self.data=[None]*capacity

    def get(self,index):
        if index>self.size:
            raise IndexError("index is illegal")

        return self.data[index]


    def get_capacity(self):
        return len(self.data)

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def addlast(self,value):
        self.add(self.size,value)

    def add(self,index,value):
        if index>self.size:
            raise IndexError("index is illegal")

        i=self.size-1
        while i>=index:
            self.data[i+1]=self.data[i]
            i-=1
        self.data[index]=value
        self.size+=1

    def swap(self,index,parent_index):
        if index>len(self.data) or parent_index>len(self.data):
            raise IndexError("index error")

        self.data[index],self.data[parent_index]=self.data[parent_index],self.data[index]
    def remove(self,index):
        if index>=len(self.data):
            raise IndexError("index over range")
        tmp_lis=[]
        tmp_lis[:]=self.data[:index]+self.data[index+1:]
        ret=self.data[index]
        self.data[:]=[]
        self.data[:]=tmp_lis[:]
        self.size-=1
        return ret
    def remove_last(self):
        return self.remove(self.size-1)




class Max_heap(array):

    def __init__(self):
        """
        二叉堆是一颗完全二叉树。实质也就是一个数组，索引值有特殊含义，val为每棵二叉堆的节点。
        """
        self.data=array()
        self.size=0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def parent_index(self,index):
        if index==0:
            raise IndexError("root hasn't parents")

        return (index-1)//2

    def left_child_index(self,index):
        return (2*index)+1

    def right_child_index(self,index):
        return (2*index)+2

    def add(self,value):
        self.data.addlast(value)
        self.sift_up(self.data.get_size()-1)
        self.size+=1

    def sift_up(self,index):
        #若二叉堆有多个节点，且index的父亲节点小于子节点的话，就进行上移操作。
        while index>0 and (self.data.get(self.parent_index(index))-self.data.get(index))<0:
            #交换两个节点的val
            self.data.swap(index,self.parent_index(index))
            #更改索引
            index=self.parent_index(index)

    def find_max(self):
        if self.data.get_size()==0:
            raise IndexError("can not findMax when heap is empty")
        return self.data.get(0)

    def sift_down(self,index):
        #index的左孩子索引小于整个数组的索引
        while self.left_child_index(index)<self.get_size():
            ind=self.left_child_index(index)
            #有右孩子且右孩子大于左孩子(比较左右孩子的大小，然后和根节点进行互换)
            if ind+1<self.data.get_size() and (self.data.get(ind+1)-self.data.get(ind)>0):
                #获取右孩子的索引
                ind=self.right_child_index(index)

            #根节点大于左右孩子中较大的孩子，则break
            if self.data.get(index)-self.data.get(ind)>=0:
                break

            #其他情况的话，则替换根节点和孩子节点的值，并将孩子节点设为根节点接着循环
            self.data.swap(index,ind)

            index=ind


    def extract_max(self):
        ret = self.find_max()

        #替换最大值和数组的最小值
        self.data.swap(0,self.get_size()-1)
        #移除最小值的索引
        self.data.remove(self.size-1)
        #下沉
        self.sift_down(0)
        return ret







if __name__ == '__main__':

    m_heap = Max_heap()

    print(m_heap.get_size())
    for i in range(1,9):
        m_heap.add(i)
    print(m_heap.get_size())
    print(m_heap.find_max())

    # print(m_heap.extract_max())


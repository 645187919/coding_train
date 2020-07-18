#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/15 21:34
# @Author : magician
# @File : array.py
# @Software: PyCharm

class array(object):
    def __init__(self,capacity=20,fillvalue=None):
        """

        :param capacity: 默认数组大小（也可定义为无大小的数组长度即list()）
        :param fillvalue: 默认填充值
        """
        self.data=list()#声明self的一个属性items,有这个属性才能做后续的操作
        self.str=""
        self.size=0

        for count in range(capacity):
            self.data.append(fillvalue)
            self.size+=1

    def get_size(self):
        return self.size

    def __str__(self):
        return str(self.data)

    def __iter__(self):
        return iter(self.data)

    def get(self, index):
        if index is None or index>=len(self.data):
            raise Exception("index is None or index over")
        return self.data[index]

    def set(self, index, new_value):
        """
        :param index:
        :param new_value:
        :return:
        """
        self.data[index]=new_value
        # self.size+=1
        return self.data

    def addlast(self,value):
        self.data.append(value)
        self.size+=1
        return self.data

    def _add(self, index,value):
        self.data.insert(index,value)
        self.size+=1
        return self.data

    def toString(self):
        for i in range(len(self.data)):
            self.str+=str(self.data[i])
            if i !=(len(self.data)-1):
                self.str+=","
        return self.str

    def contains(self, item):
        for i in self.data:
            if i==item:
                return True
        return False
    def find(self,value):

        for i in range(len(self.data)):
            if self.data[i]==value:
                return i
        return -1

    def add(self,index,value):
        """
        在指定位置添加元素：先在数组末尾扩充一位，然后将index及其之后的元素后移
        :param index:
        :param value:
        :return:
        """
        #先扩充一位
        self.data.append(1)

        if index is None or index>=len(self.data):
            raise IndexError("index error")
        #将index及其之后的元素向后移动一个位置。
        for i in range((len(self.data)-2),0,-1):
            if i>=index:
                self.data[i+1]=self.data[i]
        self.data[index]=value
        self.size+=1
        return self.data


    def swap(self,index,parent_index):
        """
        交换两个元素的位置
        :param index:
        :param parent_index:
        :return:
        """
        if index>len(self.data) or parent_index>len(self.data):
            raise IndexError("index error")

        self.data[index],self.data[parent_index]=self.data[parent_index],self.data[index]

    def remove(self,index):
        """
        移除输入索引的元素：将索引后面的元素向前移
        :param index:
        :return:
        """
        if index>=len(self.data):
            raise IndexError("index over range")
        tmp_lis=[]
        #赋值数据的值给另一个数组，而tmp_lis=arr，则代表对arr的引用
        tmp_lis[:]=self.data[:index]+self.data[index+1:]
        ret=self.data[index]
        self.data[:]=[]
        self.data[:]=tmp_lis[:]
        self.size-=1
        return ret


        # return tmp_lis



if __name__ == '__main__':
    a = array(6)
    print(a)
    print(a.get_size())
    for i in range(a.get_size()):
        # print(a.data[i])
        a.data[i]=i+1
    # print(a)
    print(a.get(3))
    print(a.set(3,100))
    print(a.addlast(200))
    print(a.add(1, 299))
    print(a.toString())
    print(a.contains(399))
    print(a.find(3))
    print(a.add(3,3))
    print(a.get_size())
    print(a.remove(3))
    print(a.get_size())




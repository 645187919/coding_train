#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/17 20:12 
# @Author : magician 
# @File : BET.py 
# @Software: PyCharm

class Node(object):
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

class BET(object):
    def __init__(self):
        #根节点
        self.root=None
        self.size=0


    def add(self,val):
        """
        二分搜索树添加一个元素的操作
        :param val:
        :return:
        """
        # 方法一
        if self.root == None:
            self.root=Node(val)
            self.size+=1
        else:
            #由于二分搜索树以链表的形式存储数据，所以需要不断的递归查找数据。
            self.__add(self.root, val)

        # # 方法二:使节点与二分搜索树相连
        # self.root=self.__add(self.root,val)
    #私有方法
    def __add(self,node,val):
        #终止条件：若二分搜索树为none或者找到一个空的节点位置。
        if node is None:
            self.size+=1
            return Node(val)
        # 递归添加
        #若根节点大于val，则递归的和左子节点比较大小
        if node.data>val:
            node.left=self.__add(node.left,val)
        elif node.data<val:
            node.right=self.__add(node.right,val)
        
        #返回叶子节点
        return node
    
    def pre_order(self):
        """
        二分搜索树的前序遍历即DFS
        :return:
        """
        self.__pre_order(self.root)

    def __pre_order(self, root):

        #递归方法先考虑停止条件：即当节点为None时，停止遍历。
        if root==None:
            return
        print(root.data)
        self.__pre_order(root.left)
        self.__pre_order(root.right)

     #
    def contains(self,val):
        """
        二分搜索树查找一个元素的操作
        :param val:
        :return:
        """
        return self.__contains(self.root,val)

    def __contains(self, root, val):
        """

        :param root:
        :param val:
        :return:
        """
        #若传入节点为None（两种情况：1、root为none；
        # 2、遍历到叶子节点的子节点时依旧没找到满足的目标值）。即当节点为None时，代表无满足条件的val；
        if root==None:
            return False
        #若传入节点的值和目标值相等
        if root.data==val:
            return True
        #若传入节点的值大于目标值，则去左子树递归查找。
        elif root.data>val:
            return self.__contains(root.left,val)
        else:
            return self.__contains(root.right,val)


    def level_order(self):
        """
        二分搜索树的层序遍历即BFS
        :return:
        """
        #整体的逻辑：首先通过队列来依次获取父节点，然后弹出该父节点，再依次将该父节点的左右孩子节点
        #加入队列。以此不断的迭代。即采用广度优先的方法来遍历。
        q=list()
        q.append(self.root)
        while len(q)!=0:
            cur = q.pop(0)
            print(cur.data)
            if cur.left!=None:
                q.append(cur.left)
            if cur.right!=None:
                q.append(cur.right)



bet = BET()
nums=[5,3,6,8,4,2]
for i in nums:
    # print(bet.add(i))
    bet.add(i)
print(bet.pre_order())
print(bet.contains(5))
print(bet.contains(-1))
print(bet.level_order())
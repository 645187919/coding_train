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
        # 方法一
        if self.root == None:
            self.root=Node(val)
            self.size+=1
        else:
            self.__add(self.root, val)

        # # 方法二:使节点与二分搜索树相连
        # self.root=self.__add(self.root,val)

    #私有方法
    def __add(self,node,val):

        #若二分搜索树为none
        if node is None:
            self.size+=1
            return Node(val)

        # 递归添加
        if node.data>val:
            node.left=self.__add(node.left,val)
        elif node.data<val:
            node.right=self.__add(node.right,val)
        
        #返回叶子节点
        return node
    
    def pre_order(self):
        self.__pre_order(self.root)

    def __pre_order(self, root):
        #递归方法先考虑停止条件
        if root==None:
            return
        print(root.data)
        self.__pre_order(root.left)
        self.__pre_order(root.right)

     #
    def contains(self,val):

        return self.__contains(self.root,val)




    def __contains(self, root, val):
        if root==None:
            return False
        if root.data==val:
            return True
        elif root.data>val:
            return self.__contains(root.left,val)
        else:
            return self.__contains(root.right,val)


    def level_order(self):
        #整体的逻辑：若队列不为空，则先取出队首的值，然后判断其左右孩子节点是否为空，不为空，则加入队列。
        # （即每取出一个节点，就去判断该节点的是否有孩子节点，然后存入队列）
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
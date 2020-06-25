#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/25 15:36 
# @Author : magician 
# @File : BET.py 
# @Software: PyCharm


class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None





class BET(object):
    def __init__(self):
        #二叉树只需要声明对应的基本结构：即Node和size。对应的data和左右孩子则在Node中进一步声明。
        self.root=None
        self.size=0

    def  get_size(self):
        return self.size
    def is_empty(self):
        return self.size==0

    def add(self,val):
        # 方法一：和下面方法一配对
        # #如果当前二叉树为空，则将创建根节点。
        # if self.root==None:
        #     self.root=Node(val)
        #     self.size+=1
        # #否则将新插入的val放入根节点的子节点中
        # else:
        #     self.add(self.root,val)

        # 方法二:
        self.root = self._add(self.root, val)

    # 后续的添加操作实质也就是传入node和val，然后查看
    def _add(self,node,val):
          # 方法一：
          # #在“根”节点(整个树结构可以看做是多个“根”节点的递归调用)插入val，
          # # 若该节点存在val,则return;否则判断val与节点的val大小关系再决定要插入哪边
          # if self.root.data==val:
          #     return
          # elif self.root.data>val and self.root.left==None:
          #     self.root.left=Node(val)
          #     self.size+=1
          #     return
          #
          # elif self.root.data<val and self.root.right==None:
          #     self.root.right=Node(val)
          #     self.size+=1
          #     return
          # #递归调用（此时“根”节点已变为root.left/right节点）
          # if self.root.data>val:
          #     self.add(self.root.left,val)
          # else:
          #     self.add(self.root.right,val)


          # 方法二：返回插入新节点后的二叉树的根。
          #若根节点为None
          if node is None:
              self.size+=1
              return Node(val)

          if node.data>val:
              #将val插入left后，再将left作为“根”节点
              node.left = self._add(node.left, val)
          elif node.data<val:
              node.right=self._add(node.right,val)

          return node


    def contains(self,val):
        return self._contains(self.root,val)

    def _contains(self,node,val):
        #若为None，则返回False，否则判断每个节点的值与val的大小
        if node==None:
            return False
        if node.data==val:
            return True
        elif node.data>val:
            return self._contains(node.left,val)
        else:
            return self._contains(node.right,val)

    #遍历实质也就是先看根节点的val,然后递归看他的左右孩子节点
    def _pre_order(self,node):
        if node==None:
            return
        print(node.data)
        self._pre_order(node.left)
        self._pre_order(node.right)




    #
    def pre_order(self):
        self._pre_order(self.root)




if __name__ == '__main__':
    bet = BET()
    # node=Node(2)
    # print(bet.size)
    # print(bet.add(node, 1))
    # print(bet.size)
    # print(node.left.data)
    # print(bet.add(node.left,-1))
    # print(bet.size)
    # print(node.left.left.data)
    nums=[5,3,6,8,4,2]
    for i in nums:
        bet.add(i)
    bet.pre_order()

    print(bet.contains(5))

    print(bet.contains(-1))


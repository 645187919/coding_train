#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/25 15:36 
# @Author : magician 
# @File : BET.py 
# @Software: PyCharm


class Node(object):
    #二叉树的node
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
        """
        节点是否包含某个val
        :param node:需要传入初始的根节点
        :param val:
        :return:
        """
        #若为None，则返回False，否则判断每个节点的值与val的大小
        #两个递归终止条件：节点为None，节点data等于val。
        if node==None:
            return False
        if node.data==val:
            return True
        #递归的逻辑（递归的基本问题）：看val与data的大小关系。再与其孩子节点做比较，直到达到终止条件。
        elif node.data>val:
            return self._contains(node.left,val)
        else:
            return self._contains(node.right,val)

    def _pre_order(self,node):
        """
        先续遍历：遍历实质也就是先看根节点的val,然后递归看他的左右孩子节点
        :param node:
        :return:
        """
        if node==None:
            return
        print(node.data)
        self._pre_order(node.left)
        self._pre_order(node.right)


    def pre_order(self):
        self._pre_order(self.root)



    def _in_order(self,node):
        """
        递归写法：若节点不为空，则对于每一个递归的“单元”先看左孩子，再看“根”节点后看右孩子。
        :param node: 需要处理的节点（二分树每个节点）
        :return:
        """
        if node is None:
            return
        self._in_order(node.left)
        print(node.data)
        self._in_order(node.right)


    def in_order(self):
        """
        中序遍历
        :return:
        """
        self._in_order(self.root)


    def level_order(self):
        """
        层序遍历
        :return:
        """
        #以一个队列来存储数据，先进先出
        q=list()
        q.append(self.root)
        while len(q)!=0:
            #整体的逻辑：若队列不为空，则先取出队首的值，然后判断其左右孩子节点是否为空，不为空，则加入队列。
            # （即每取出一个节点，就去判断该节点的是否有孩子节点，然后存入队列）
            cur = q.pop(0)
            print(cur.data)
            if cur.left!=None:
                q.append(cur.left)
            if cur.right!=None:
                q.append(cur.right)
    def _find_min(self,node):
        if node.left==None:
            return node.data
        return self._find_min(node.left)

    def find_min(self):
        return self._find_min(self.root)

    def _find_max(self,node):
        if node.right==None:
            return node.data
        return self._find_max(node.right)

    def find_max(self):
        return self._find_max(self.root)

    def _remove_min(self,node):
        """
        删除掉以node为根的二分搜索树中的最小节点
        返回删除节点后新的二分搜索树的根
        :param node:
        :return:
        """
        #终止条件：若node的left为None,则将该node删除；怎么删除，实质也就让node的right替代node
        if node.left is None:
            right_node = Node(-1)
            right_node=node.right
            node.right=None
            self.size-=1
            return right_node
        #实质问题：删除子节点的left子节点。
        node.left = self._remove_min(node.left)
        return node

    def remove_min(self):
        min = self.find_min()
        self.root = self._remove_min(self.root)
        return min


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

    bet.in_order()
    print("#"*10)

    bet.level_order()
    print("#"*10)

    print(bet.find_min())
    print(bet.find_max())

    print(bet.remove_min())
    print(bet.size)

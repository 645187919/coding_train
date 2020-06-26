#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2020/6/26 15:51 
# @Author : magician 
# @File : BET_set.py 
# @Software: PyCharm

from data_structure.BET import BET


class BET_set(BET):
    def __init__(self):
        self.bet_set=BET()

    def get_size(self):
        return self.bet_set.size

    def is_empty(self):
        return self.bet_set.size==0

    def contains(self,val):
        return self.bet_set.contains(val)

    def add(self,val):
        self.bet_set.add(val)

    def remove_min(self):
        self.remove_min()
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/18 21:06 
# @Author : magician 
# @File : python_genericity.py 
# @Software: PyCharm


from functools import singledispatch
@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)
@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)
@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

print(fun(42, verbose=True))
print(fun(['spam', 'spam', 'eggs', 'spam'], verbose=True))
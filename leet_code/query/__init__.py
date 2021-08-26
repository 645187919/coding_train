#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-26 20:17 
# @Author : magician 
# @File : __init__.py.py 
# @Software: PyCharm

#
dic={"a":1,"b":2}
print(dic.values())
#
# print(dic["a"])
# # print(dic["c"])
# for i in dic.items():
#     print(i)
#     print(i[0])
# print(len(dic))
#
# a=123
# for i in a:
#     print(i)
# str="dog cat cat dog"
# b="abba"
# print(b[1])
# res=str.split()
# print(map(res.index, res))
# print(list(map(res.index, res)))


a = [1,2,1]
b = [4,5,6]
zipped = zip(a,b)
print(zipped)
for i in zipped:
    print(i)

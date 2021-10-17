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
for i in dic.items():
    print(i)
    print(i[0])
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


# a = [1,2,1]
# b = [4,5,6]
# zipped = zip(a,b)
# print(zipped)
# for i in zipped:
#     print(i)

# a = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 5,
#     'a': 2
# }
#
# print(a)
#
# nums = [-1,0,1,2,-1,-4]
# print(nums.sort())
# print(nums)
# table = {val: index for index, val in enumerate(nums)}
# print(table)
# len_nums=5
# for j in range(5, 2, -1):
#     print(j)
# def containsNearbyAlmostDuplicate(nums, k,t) -> bool:
#
#     #abs(i-j)<=k代表子串的长度小于k，即在长度小于k的子串中寻找满足abs(num[i]-nums[j])<=t的数
#     nums_len=len(nums)
#     nums.sort()
#     print(nums)
#
#     for l in range(nums_len-1):
#         print(l)
#         print(l+1)
#         print(l+k)
#         for r in range(l+1,l+k):
#             print(r)
#             print(nums[l])
#             print(nums[r])
#             if abs(nums[l]-nums[r])<=t:
#                 return True
#             else:
#                 break
#     return False
#
#
# print(containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))

tmp={'t': 1, 'r': 1, 'e': 2}
print([(key,val) for key,val in tmp.items()])


# res=[('b', 2),('a', 1),  ('c', 3), ('d', 4)]
# print(res)
# res_1=sorted(res,key=lambda x:x[1])
# print(res_1)

lisa=[1,3,2]
lisa.sort()
print(lisa)

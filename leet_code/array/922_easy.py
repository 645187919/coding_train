#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-22 21:34 
# @Author : magician 
# @File : 922_easy.py 
# @Software: PyCharm


# 922. 按奇偶排序数组 II
# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
# 你可以返回任何满足上述条件的数组作为答案。
#
# 示例：
# 输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#
# 提示：
#
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000

# 参考：https://leetcode-cn.com/problems/sort-array-by-parity-ii/solution/922san-chong-po-shi-wu-hua-de-fang-fa-ren-ni-xuan-/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        #方法1：用多个数组；
        # nums_len=len(nums)
        # tmp1=[]
        # tmp2=[]
        # for i in nums:
        #     if i%2==0:
        #         tmp1.append(i)
        #     else:
        #         tmp2.append(i)

        # for i in range(nums_len):
        #     if i%2==0:
        #         result=tmp1.pop()
        #         nums[i]=result
        #     else:
        #         result=tmp2.pop()
        #         nums[i]=result
        # return nums

        #方法2：双指针
        #left维护偶数,right用于遍历
        left=1
        len_nums=len(nums)
        for right in range(0,len_nums,2):
            #若偶数索引位为奇数的话
            if nums[right]%2==1:
                #看奇数索引下的值,若为奇数，则不断的移动索引
                while nums[left]%2==1:
                    left+=2
                #若为偶数，则交换left和right索引的值
                nums[left],nums[right]=nums[right],nums[left]
        return nums
















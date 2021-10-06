#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-09-04 15:14 
# @Author : magician 
# @File : 108_easy.py 
# @Software: PyCharm

# 108. 将有序数组转换为二叉搜索树
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

# 示例 1：
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
#
# 示例 2：
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。
#
#
# 提示：
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums 按 严格递增 顺序排列

#思路参考：（很好的文章）
#https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/solution/yi-wen-du-dong-shi-yao-shi-er-cha-sou-suo-shu-bst-/
#知识点1、我们发现，前序，后续，中序遍历
# 这个“前”、“中”、“后”其实指的就是ROOT在遍历当中的位置嘛，左右两部分则一直都是从左到右。

#知识点2：比如中序遍历的过程，遍历的时候，记住一个关键点：
#####我们遍历的是树而不是节点#####
# 这么说有点抽象，具体一点说：每次遍历的时候，要把子树看成一个整体，
# 比如我们来看一个最大的格局：爸爸节点是1号，那么左子树是2、4、5、7、8整个整体，
# 右子树是3、6、9、10整个整体，
# 在这个最大格局上进行遍历，那就是左子树整体->1号->右子树整体
#  
# 所以我们现在知道要从左子树开始，那么左子树也要遵循中序遍历，所以顺序应该是
# 4、7整体 -> 2 -> 5、8整体
#  
# 然后进入1
#  
# 然后进入右子树，右子树也遵循中序遍历：
# 空白(3开头的右子树并没有左边部分) -> 3 -> 6、9、10整体
#  
# 依此类推，如果你能理解完整的顺序：
# 4、7、2、8、5、1、3、9、6、10
# 说明你已经理解了中序遍历，记住每次进入一个子树的时候，不要急着先遍历这个子树的爸爸，每个子树也都是要从左边开始才能是中序遍历的！


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        #手写的过程
        def make_tree(start_index,end_index):#只和长度有关
            #首先判定我们的区间是否合理，即left_index要<=right_index
            #当相等时，只有root会产生，不会产生左右小树
            #递归的构造树。
            #到达叶子节点停止构造；
            #否则依次递归的构造根节点的左右子节点
            if start_index>end_index:
                return None
            mid_index=(start_index+end_index)//2
            #根节点
            tree_root=TreeNode(nums[mid_index])
            #递归的构造左子树
            tree_root.left=make_tree(start_index,mid_index-1)
            #递归的构造右子树
            tree_root.right=make_tree(mid_index+1,end_index)
            return tree_root #做好的小树

        return make_tree(0,len(nums)-1)


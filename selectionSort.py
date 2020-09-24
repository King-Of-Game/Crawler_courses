# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# date : 2019/7/13

"""选择排序是从第一个数~倒数第二个数开始，与它后面每一个数进行比较，关键是a[i]与a[j]交换位置
   选择排序是从前往后整理好的
"""

# a = input()
# a = a.split(',')    # 把字符串用","切割成数组
# a = [int(a[i]) for i in range(len(a))]

"从小到大排序"

# a = [2,3,5,6,7,1,9,8,10,4]

# for i in range(0, len(a)-1):  # 被比较数从索引'0'开始，直到倒数第二个数才结束
#     for j in range(i+1, len(a)):  # 待比较数从被较数后面那个数开始，直到最后那个数才结束
#         if a[i] > a[j]:
#             temp = a[j]
#             a[j] = a[i]
#             a[i] = temp
#
# print(a)


"""从大到小"""
# list1 = [1,3,5,7,9,2,4,6,8,10]
# length = len(list1)
#
# for i in range(length-1):
#     for j in range(i+1,length):
#         if list1[j] > list1[i]:
#             temp = list1[j]
#             list1[j] = list1[i]
#             list1[i] = temp
#
# print(list1)








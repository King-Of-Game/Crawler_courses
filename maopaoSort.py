# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# date : 2019/7/13

"""冒泡排序首先要知道比较的趟数，然后每一趟都从数组第一个数开始~数组长度-趟数，两两比较，关键是a[j]与a[j+1]交换位置
   冒泡排序是从后往前整理好的
"""

"""从小到大"""

a = [4,5,3,6,1,2]
length = len(a)
temp = 0


for i in range(0, length-1):    # 变量i代表比较的趟数，i等于数组长度-1
    for j in range(0, length-1-i):  # 变量j代表每趟两两比较的次数
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print(a)


"""从大到小"""
# list1 = [1,3,5,7,9,2,4,6,8,10]
# length = len(list1)
# for i in range(length-1):
#     for j in range(0, length-1):
#         if list1[j+1] > list1[j]:
#             temp = list1[j+1]
#             list1[j+1] = list1[j]
#             list1[j] = temp
# print(list1)

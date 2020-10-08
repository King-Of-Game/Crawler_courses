# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# date : 2019/7/13

'''
冒泡排序：从小到大排序
每轮都从第一个元素开始，相邻的两个元素比较，把大的放后面（从后往前排序）
'''
def maopao(a):
    length = len(a)
    for i in range(length - 1):  # 一共比较(length - 1)轮
        for j in range(length - 1 - i):  # 每轮比较的次数
            if a[j] > a[j + 1]:
                x = a[j]
                a[j] = a[j + 1]
                a[j + 1] = x
    print(a)

    # 从大到小
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if a[j] < a[j+1]:
                x = a[j]
                a[j] = a[j+1]
                a[j+1] = x
    print(a)


if __name__ == '__main__':
    a = [4, 5, 3, 6, 1, 2]
    maopao(a)
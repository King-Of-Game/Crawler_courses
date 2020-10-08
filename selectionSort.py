# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# date : 2019/7/13

'''
选择排序：从小到大排序
第一轮从第1个元素开始（第二轮第2个....），依次跟后面所有的元素比较，把小的放前面（从前往后排序）
'''
def select(a):
    length = len(a)
    for i in range(length - 1):  # 总共比较（length - 1）轮
        for j in range(i+1, length):  # 第i个元素依次和后面的比较
            if a[i] > a[j]:
                x = a[i]
                a[i] = a[j]
                a[j] = x
    print(a)

    # 从大到小
    for i in range(length - 1):
        for j in range(i+1, length):
            if a[i] < a[j]:
                x = a[i]
                a[i] = a[j]
                a[j] = x
    print(a)


if __name__ == '__main__':
    a = [4, 5, 3, 6, 1, 2]
    select(a)








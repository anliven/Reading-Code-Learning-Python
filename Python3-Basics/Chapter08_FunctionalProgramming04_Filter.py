#! python3
# -*- coding: utf-8 -*-


def is_even(x):
    return x % 2 == 0


f_sample = filter(is_even, [0, 1, 2, 3, 4, 5, 6])
print(f_sample)
for var in f_sample:  # for循环遍历迭代器
    print(var)


def not_empty(s):
    return s and s.strip()


f_sample2 = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))  # 删除序列中的空字符串
print(f_sample2)
for var in f_sample2:
    print(var)

f_sample3 = ("hello", "Python", "world")
result = filter((lambda x: x.find("hello") != -1), f_sample3)  # 筛选出字符串元组中包含hello的所有字符串
for i in result:
    print(i)

f_sample4 = ["abcde", "12345", "hello", "python"]
result = filter((lambda x: len(x) == 6), f_sample4)  # 筛选出字符串列表中长度为6的字符串
for i in result:
    print(i)

# ### filter函数
# Python内建的filter()函数用于过滤序列；
# filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list;
# 接收两个参数：一个函数和一个序列；
# filter()将函数作用在序列的每个元素，根据函数返回值True或False，决定是否舍弃该元素，最终返回一个迭代器，内容是原序列的子序列；
# filter()函数返回的是一个惰性Iterator序列，但可以使用list()函数获得所有结果并返回list；
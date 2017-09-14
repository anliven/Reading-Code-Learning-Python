#! python3
# -*- coding: utf-8 -*-

print(-7)
print(2 * 3)
print('Test' * 3)
print(10 / 3)  # 注意观察实际结果

print(11 >> 1)
print(~555)

print(3 < 5 < 7)

x = "vvv"
y = 123
print(not x)
print(x and y)  # 如果x是False，则返回False，否则返回y的计算值
print(x or y)  # 如果x是True，则返回True，否则它将返回y的计算值；

length = 5  # 长度（Length）
breadth = 3  # 宽度（Breadth）
area = length * breadth  # 面积（Area）
print('Area is', area)  # 注意观察输出的结果，Python自动添加了空格
print('Perimeter is', 2 * (length + breadth))  # 周长（Perimeter）

# ### 表达式（Expressions）
# - 表达式可以拆分成运算符（Operators）与操作数（Operands）；
# - 运算符表明进行何种运算操作，操作数是被操作的数据；

# ### 运算符（Operators）
# + （加）：x加y；
# - （减）：x减y，如果x不存在，则假定为零；
# * （乘）：x乘y，或返回字符串重复指定次数后的结果；
# / （除）：x除以y；
#
# ** （乘方）：x的y次方；
# // （整除）：x除以y并对结果向下取整；
# % （取模）：x除以y运算后的余数；
#
# << （位左移）：将数字的位向左移动指定的位数；（每个数字在内存中以二进制数表示，即0和1）
# >> （位右移）：将数字的位向右移动指定的位数；
# & （按位与）：对数字进行按位与操作；
# | （按位或）：对数字进行按位或操作；
# ^ （按位异或）：对数字进行按位异或操作；
# ~ （按位取反）：x的按位取反结果为-(x+1)；
#
# < （小于）：返回x是否小于y；所有的比较运算符返回的结果均为首字母大写的True或False；
# > （大于）：返回x是否大于y；
# <= （小于等于）：返回x是否小于或等于y；
# >= （大于等于）：返回x是否大于或等于y；
# == （等于）：比较两个对象是否相等；
# != （不等于）：比较两个对象是否不相等；
#
# not （布尔“非”）：如果x是True，则返回False；如果x是False，则返回True；
# and （布尔“与”）：如果x是False，则返回False，否则返回y的计算值；适用短路计算（Short-circuit Evaluation）；
# or （布尔“或”）：如果x是True，则返回True，否则它将返回y的计算值；适用短路计算；

# ### 数值运算与赋值的快捷方式
# “变量 = 变量 运算 表达式”等同于“变量 运算 = 表达式”；

# ### 求值顺序
# - Python 将优先执行高优先级的运算符与表达式；
# - 相同优先级的运算符将从左至右的方式依次进行求值；
# - 使用圆括号可以改变运算的顺序；
# - 建议使用圆括号操作符来对运算符与操作数进行分组，更加明确地指定优先级，使得程序更加可读；

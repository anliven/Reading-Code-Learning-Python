# -*- coding: utf-8 -*-
__author__ = 'Anliven'

import random  # 模块名称使用不带下划线的小写字母。若是它们实现一个协议，那么通常使用lib为后缀。


class BaseFruit:  # 对于基类而言，可使用一个 Base 或者 Abstract 前缀
    AVG_PRICE = 5  # 大写加下划线,仅用来标明是不会发生改变的全局变量
    __a = 22  # 双下划线开头的变量，表示名字改编

    def __init__(self):  # 双下划线开头双下划线结尾的函数，Python的魔术方法（内置方法/特殊方法）
        self.__color = "red"  # 双下划线开头的变量，表示名字改编
        self.__code = 11  # 双下划线开头的变量，表示名字改编


class Apple(BaseFruit):  # 驼峰格式命名，即所有单词首字母大写其余字母小写。类名应该简明，精确。
    __b = 10  # 双下划线开头的变量，表示名字改编
    _c = "200g"  # 小写和一个前导下划线,仅用于警告说明外部类不要去访问它

    @staticmethod
    def _apple_price():  # 单下划线开头，名称末尾没有下划线，仅用于警告说明外部类不要去访问这个函数。
        return random.randint(5, 10)


if __name__ == "__main__":
    one = Apple()
    print one.__dict__  # 打印对象one的实例属性
    print dir(one)  # 打印对象one所有有效属性
    print one._apple_price()  # 仍然可以访问到
    print one._c  # 仍然可以访问到
    AVG_PRICE = 3
    print AVG_PRICE  # 仍然可以改变值

#     print AppleNumber.__dict__
#     print dir(AppleNumber)


# python 的下划线含义

# 大写加下划线的变量: 标明是不会发生改变的全局变量。

# 单下划线开头，名称末尾没有下划线。
# 变量---用于警告说明外部类不要去访问这个变量，但实际上外部类还是可以访问到这个变量。
# 函数---用于警告说明外部类不要去访问这个函数。
# 在一个模块（例如a_module）中以单下划线开头的变量和函数相当于“私有变量”和“私有函数”，不希望外部的类访问它们。
# 使用 from a_module import * 导入时，这部分变量和函数不会被导入。
# 但如果使用 import a_module 导入模块，仍然可以用 a_module._some_var 这样的形式访问到这样的对象。

# 单下划线结尾的样式
# 在解析时并没有特别的含义，但通常用于和 Python 关键词区分开来
# 例如： 定义一个变量叫做 class，但 class 是 Python 的关键词，此时可以以单下划线结尾写作 class_。

# 双下划线开头，名称末尾没有下划线。
# 在 Python 的类成员中使用，表示名字改编 (Name Mangling)。
# 例如：Test 类里有一成员 __x，那么 dir(Test) 时会看到 _Test__x 而不是 __x。
# 可用于避免该类成员的名称与子类中的名称冲突。

# 双下划线开头双下划线结尾
# 变量---标明是内置变量
# 函数---Python的魔术方法，例如：类成员的 __init__、__del__、__add__、__getitem__ 等，以及全局的 __file__、__name__ 等。
# Python 官方推荐永远不要将这样的命名方式应用于自己的变量或函数，而是按照文档说明来使用。


# Python 的代码风格
# Python 的代码风格由 PEP 8 描述。
# 在遵守这个文档的条件下，不同程序员编写的 Python 代码可以保持最大程度的相似风格。易于阅读和程序员之间交流。
# 可以安装一个 pep8 用于验证你的代码风格是否符合 PEP8 规范。

#! python3
# -*- coding: utf-8 -*-


class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':  # 当模块正常导入时，doctest不会被执行；只有在命令行直接运行时，才执行doctest
    import doctest

    doctest.testmod()

# ### 文档测试（doctest）
# Python内置的doctest模块可以直接提取注释中的代码并执行测试;
# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确;
# 在测试异常的时候，可以用...表示中间大段的输出；
# 如果没有信息输出，说明编写的doctest运行都是正确的；

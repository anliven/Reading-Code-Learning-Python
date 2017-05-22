# -*- coding: utf-8 -*-
# 中文字符显示需要上一行的内容“# -*- coding: utf-8 -*-”来声明编码，文件本身也需要保存成UTF-8格式。
import os  # 导入模块，这里导入了名称为OS的模块,其实是导入了os.py

__author__ = 'Anliven'  # 标明作者


# def 用来声明函数，使用冒号来结束声明
def main():  # 函数名main在这里并不是必须的，调用在此脚本的最后部分
    # python使用缩进来代替其他语块声明，一般建议每个层级用4个空格来缩进
    print 'Hello World!'  # 使用单引号或双引号声明单行字符串
    print "这是来自Anliven\'的问候！"  # 注意字符串中对引号的转义处理， “\”为转义字符

    foo(5, 10)  # 函数调用，这里调用了名称为foo的函数

    print '=' * 10  # 字符可以相乘
    print '这将直接执行'+os.getcwd()  # “+”可以用来连接字符串；调用os模块的getcwd函数

    counter = 0  # 实例化一个变量。变量必须先实例化才可以进一步使用。
    counter += 1  # 对变量做运算。“+=”是加法赋值运算符， a += b 等效于 a = a + b

    food = ['苹果', '0123456789', 'physics']  # 创建列表；列表可以包含不同类型数据
    for name in food:  # 在for in循环中使用冒号结束声明；这个循环中的name指代了列表中按顺序的数据项
        print '列表：'+name

    print '数到9'
    for number in range(10):  # range()为内置函数
        print number


def foo(param1, param2):
    res = param1+param2
    print '%s 加 %s 等于 %s' % (param1, param2, res)  # 字符串的格式化输出
    if res < 50:  # “<”是python的运算符之一；用冒号来结束判断语句
        print '这个'
    elif (res >= 50) and ((param1 == 42) or (param2 == 24)):  # “and”和“or”都是Python的逻辑运算符
        print '那个'
    else:  # 用冒号来结束判断语句，在if、elif、else之后
        print '嗯......'
    return res  # 这里是单行注释

'''这里是多
行注释示例'''

if __name__ == "__main__":
    main()
# 一般测试代码是安置的在脚本最后调用主函数main();
# 使用内置的运行脚本名来判定，当且仅当直接运行当前脚本时，__name__才为__main__;
# 当脚本被当做模块进行import导入时，并不运行main();
# 所以一般情况下，是在测试代码时，才需要添加“判定__name__后调用main()”的部分；
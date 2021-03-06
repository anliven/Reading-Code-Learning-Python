# doctest
- Python自带的简单自动化测试工具，是基于文档的测试，用于检查文档，也可用于简单一点的单元测试；
- 文档格式要求：测试用例都要和Python交互方式下的输入输出一致，而其他格式的文字可以当作是注释；
- doctest的好处在于写代码的同时就写下了测试代码，而且又是很好的注释，但适用于简单的测试过程；
- 更多内容请查看：https://docs.python.org/3/library/doctest.html



# 简单示例
- doctest使用Python object的__doc__来记录对应module、class、method测试的测试用例；
- doctest的书写形式就是在Python CLI中交互执行程序时输入输出的形式；

## 创建测试用例
Python文件func.py有如下内容：
```python
def func(arg):
    print(arg)
```
对于这样一个method，在Python CLI下交互执行的输入输出过程如下：
```
>>> def func(arg):
...     print(arg)
...
>>>
>>> func(1)  # 这是输入
1  # 这是输出
>>>
```

使用doctest来写一个TestCase，就是直接把上面的输入输出执行过程写进func的__doc__里面，
例如：创建一个Python文件test_func.py；
```python
def func(arg):
     """TestCase for fun
     >>> func(1)
     1
     """
     print(arg)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

## 测试执行过程
- 在当前目录命令行下执行“python test_func.py”，__doc__里面以>>>开始的代码会被执行，并检查执行的输出；
- “python test_func.py -v”，加上参数-v，则会在打印出每个尝试的细节日志，并在最后给出一个统计概要；
- 测试过程： func(1)会被执行，而执行的返回值会用来于1作比较，等于1则TestCase通过，否则是就这个TestCase没过；
- 将输出的“1”改为其他数值，再执行测试将无法通过，并会给出报错信息；
- Python2.6之后，可直接执行语句
“python -m doctest -v test_func.py”来检测（不需要if语句部分）；

## 一些建议
- 将写在doctest中的内容合理编排，说明和测试用例的层次区分清晰，将有助于快速理解；
- 只要格式正确，在CLI调试时的内容可以直接贴进去当测试用例；
- 对于单元测试把测试用例和代码放在一起，对于测试和修改都是有好处的；
- doctest中”短小精悍“的测试用例适用于简单的测试过程，详细测试建议使用unittest或者nose；



# 另一个例子
待测试代码：
```python
def square(x):
    return x*x
```
测试用例：
```python
def square(x):
    """
    Squares a number and returns the results.
    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x*x
```

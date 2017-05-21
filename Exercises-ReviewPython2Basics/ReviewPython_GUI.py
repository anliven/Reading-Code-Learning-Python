# -*- coding: utf-8 -*-
__author__ = 'Anliven'

# ----------------------------------------------------------------------------------------------------------------------
### Python有多个图形开发界面的库，常用的Python GUI库如下：

# Tkinter
# Tkinter是Python自带的标准GUI库，只要安装好Python之后就能import Tkinter库。可用于快速的创建GUI应用程序
# Tkinter是对图形库TK的封装。
# Tkinter是跨平台的，在windows下编写的脚本，可以不加修改的在linux,unix等系统下运行。

# wxPython
# wxPython是一款开源软件，是跨平台GUI工具库wxWidges的封装，使用与wxWidgets相同的许可证。
# wxWidgets是一个开源的跨平台的C++构架库（framework），它可以提供GUI（图形用户界面）和其它工具。
# 利用wxPython可以方便的创建完整的、功能键全的GUI用户界面。

# PyQt
# PyQt是对Qt的封装。Qt是面向对象的图形用户界面库，是目前最强大的GUI库之一，可以在多个操作系统上使用。
# Qt虽然是开源GUI库，但其许可证限制较复杂，PyQt采用双许可证，开发人员可以选择GPL和商业许可。。

# pyGTK
# pyGTK是对GTK的封装。通过使用pyGTK模块可以在python中使用GTK创建GUI界面。
# GTK是开源的图像用户界面库。虽然GTK是使用C语言编写的，但其使用了类的思想。可以运行多种操作系统上。

# PythonWin
# PythonWin通过扩展的形式对MFC的函数进行封装。
# 通过使用PythonWin中的win32gui和win32ui模块可以调用windows API,或者使用MFC来创建GUI界面，仅适用于windows平台


# ----------------------------------------------------------------------------------------------------------------------
### 简单举例： Tkinter 编程

from Tkinter import *  # 导入Tkinter模块


def resize(NONE):
    label_1.config(font='Helvetica -%d bold' % scale.get())

root = Tk()  # 生成root主窗口（也可叫做顶层窗口或者根窗口，用于放置其他窗口、组件或者控件，包括标签，按钮，列表框等等。）
root.geometry('300x200')  # 设置主窗口的初始大小为125x100

label_1 = Label(root, text="你好，Tkinter！", fg="red", font="Helvetica -16 bold")
# 利用Tkinter的Label方法创建label_1标签:显示内容、字体颜色和大小
label_1.pack(fill=Y, expand=1)  # 将标签添加到root主窗口

TestButton = Button(root, text="TestButton")  # 创建TestButton按钮
TestButton.pack(side=BOTTOM)  # 将TestButton添加到root主窗口的底部

QuitButton = Button(root, text='QUIT', command=root.quit, activeforeground="white", activebackground="red")
QuitButton.pack()

scale = Scale(root, from_=16, to=40, orient=HORIZONTAL, command=resize)  # 创建进度条并设置
scale.set(12)  # 设置起始位置
scale.pack(fill=X, expand=1)

root.mainloop()  # 进入消息循环（主循环）

# Tkinter的窗口和组件中显示中文
#   在“.py”脚本文件中的首行添加“#-*-coding:utf-8-*-”指明字符编码
#   将脚本保存成"UTF-8"的编码格式

# ----------------------------------------------------------------------------------------------------------------------
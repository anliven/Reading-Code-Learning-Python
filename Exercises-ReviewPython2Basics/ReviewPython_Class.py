# -*- coding: utf-8 -*-

################################################################################

#面向对象把一类数据和处理这类数据的方法封装在一个类中，让程序的结构更清晰，不同的功能之间相互独立。
#类和对象是面向对象编程的主要两个方面。

#类（class）是一种抽象的类型，而对象（object）是这种类型的实例。
#类可以有属于它的函数，这种函数被称为类的“方法”。
#类方法和之前定义的函数区别在于，第一个参数必须为self。
#类/对象可以有属于它的变量，这种变量被称作“域”。域根据所属不同，分别被称作“类变量”和“实例变量”。
#域和方法被合称为类的属性。

#关键字class加上类名用来创建一个类。之后缩进的代码块是这个类的内部。
#类名加圆括号()的形式可以创建一个类的实例，也就是对象。


class MyClassPass:
    pass  # pass语句，表示一个空的代码块。

##mc = MyClassPass() # 把这个对象赋值给变量mc。于是，mc现在就是一个MyClass类的对象。
##print mc


class MyClass:  # 关键字class加上类名的形式,创建一个MyClass的类
    name = 'liven'  # 给 MyClass类增加了一个类变量name,并赋值为liven

    def sayHi(self):  # 增加一个类的方法sayHi,第一个参数必须为self，这个self是指对象本身。
        print 'hello %s' % self.name
        
##mc = MyClass()  # 类名加圆括号()的形式,创建一个MyClass类的实例,也就是对象mc
##print mc.name  # "对象.变量名"的形式调用类变量,这里得到了类变量的值
##mc.name = 'an'  # "对象.变量名"的形式调用类变量,这里改变类变量的值为'an'
#### MyClass().name = 'an'  # 通过"类名.变量名"调用类变量这种方法是错误的,类变量的值不会改变!!!
##print mc.name
##mc.sayHi()  # 以"对象.方法名"形式调用类方法,不需要额外提供self这个参数的值。

#类方法与普通的函数区别在于，第一个参数必须为self，这个self是指对象本身。
#通过“对象.方法名()”格式调用类的方法，不需要为self这个参数赋值，Python会提供这个值。
#self在类方法中的值，就是调用的这个对象本身。

################################################################################

#面向对象把一类数据和处理这类数据的方法封装在一个类中，让程序的结构更清晰，不同的功能之间相互独立。
#面向对象的继承：可以把相关的数据和方法封装在一起，并且可以把不同类中的相同功能整合起来。


#举例：从A地到B地，汽车和自行车的花费时间？汽车的油耗？
#创建一个叫做Vehicle的类，表示某种车，它包含了汽车和自行车所共有的东西：速度，行驶的动作。
#创建Car类和Bike类都继承这个Vehicle类，即作为它的子类。在每个子类中，可以分别添加各自独有的属性。
#Car类：增加一个每公里油耗的属性。Bike类不变。


class Vehicle:  # 创建Vehicle类作为基本类(超类)
    def __init__(self, speed):  # 在类被创建的时候自动调__init__函数，用来初始化类。
        self.speed = speed  # __init__函数的参数要在创建类的时候提供,初始化speed的值。

    def drive(self, distance):  # 增加一个Vehicle类的方法drive
        print 'need %f hour(s)' % (distance / self.speed) 


class Bike(Vehicle):  # class定义后面的括号里表示这个类继承于哪个类。这里Bike类具有Vehicle类的所有属性和方法。
    pass  # pass语句表示一个空的代码块。因为Bike不需要有额外的功能，所以用pass在类中保留空块，什么都不用写。


class Car(Vehicle):  # Car类是继承自Vehicle类的导出类(子类),具有Vehicle类的所有属性和方法.
    def __init__(self, speed, fuel):  # 重新定义__init__函数,覆盖了继承自Vehicle的同名函数
        Vehicle.__init__(self, speed)  # 仍然可以通过“Vehicle.函数名”来调用超类方法,获得Vehicle的属性和方法。
        # 注意，因为是通过类名调用方法，而不是像之前一样通过对象来调用，所以这里必须提供self的参数值。
        self.fuel = fuel  # 给Car增加了一个fuel属性

    def drive(self, distance):  # 重新定义drive函数,覆盖了继承自Vehicle的同名函数。
        Vehicle.drive(self, distance)  # 仍然可以通过“Vehicle.函数名”来调用超类方法,获得Vehicle的属性和方法。
        # 注意，因为是通过类名调用方法，所以这里必须提供self的参数值。
        print 'need %f fuels' % (distance * self.fuel)


#分别创建一个速度为15的自行车对象，和一个速度为80、耗油量为0.012的汽车
##bike = Bike(15.0) #类名加圆括号()的形式,创建一个Bike类的实例,也就是对象bike
##car = Car(80.0, 0.12) #类名加圆括号()的形式,创建一个Car类的实例,也就是对象car
        
#行驶100的距离的时间和油耗
##bike.drive(100.0) #以"对象.方法名"形式调用类方法
##car.drive(100.0) #以"对象.方法名"形式调用类方法

################################################################################
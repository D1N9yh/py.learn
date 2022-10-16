def caculation(a, b):
    c = a+b
    return c


result = caculation(10,20) # 按照参数位置进行实参对形参的传递
print(result)
caculation(b=10, a=20) # 关键字参数按照名称顺序进行参数传递


def fun(arg1, arg2):
    print('arg1',arg1,id(arg1))
    print('arg2',arg2,id(arg2))
    arg1 = 199
    arg2.append(19)
    print('arg1',arg1,id(arg1))
    print('arg2',arg2,id(arg2))


n1 = 12
n2 = [11,22,33,44]
print('n1',n1,id(n1))
print('n2',n2,id(n2))
fun(n1,n2)
print('n1',n1,id(n1))
print('n2',n2,id(n2))
'''在给arg1赋值以后，arg1指向的地址发生变化，n1指向的地址不变，
    arg2为可变数据类型，对列表操作不改变地址，但是列表本身的元素发生变化，arg2和n2指向同一个地址的列表于是发生变化
    函数执行完毕，arg1和arg2的内存释放，指向的地址无效
    不可变对象在函数体的修改不会影响实参的值，可变对象在函数体修改会影响实参的值
'''
'''====================================函数的返回值===================================='''
'''函数返回多个值时，返回值是元组
   如果韩叔没有返回值，return可以不写
   函数的返回值，如果是一个，直接返回原类型
   ====================================函数的形参与实参================================='''


def fun2(a, b=19):  # 默认值形参只能放在非默认值形参之后
    print(a, b)


fun2(29, 39)  # 形参默认值和实参不符时，会调用实参


def fun3(*args):  # 个数可变的位置参数
    print(args)


fun3(10)  # args可以为lst，将裂变中每个元素都作为位置实参传入
fun3(10,20)
fun3(18,20,30)
# 结果为一个元组


def fun4(**args):  # 个数可变的关键字参数
    print(args)


fun4(a=10)  # args可以为dict，将字典中每个元素都作为关键字实参传入
fun4(a=10, b=20)
fun4(a=18, b=20, c=30)
# 结果为一个字典
'''在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参
   要求个数可变的位置形参，放在个数可变的关键字形参之前。  def(*args1, **args2)
   不能同时用两个个数可变的位置形参或者关键字形参
   =====================================  '''
def fun5(a,b,*,c,d):  # 从'*'之后的参数，都只能用关键字实参传递
    return

'''==========================class类================'''
class Student:  # Student即为类名，可以由多个单词组成，每个单词首字母大写，其余小写
    native_place = '吉林'  # 直接写在类里的变量成为类属性

    # 初始化方法
    def __init__(self, name, age):
        self.name=name  # self.name称为实例属性，进行赋值操作，将局部变量name的值赋给实体属性
        self.age=age  # 源于相同类对象的不同实例对象中的属性值可以不痛
    # 实例方法（在类之外叫函数，在类之内称为方法）
    def eat(self):
        print('学生在吃饭')

    @staticmethod
    def method():
        print('这是静态方法，不能用self')

    @classmethod
    def classmethod(cls):
        print('这是类方法，加上一个cls')


student = Student('张三', '20')  # 根据类对象Student创建实例对象student
student1 = Student('张三', '20')  # 根据类对象Student创建实例对象student
student.eat()  # 对象名.方法名  实例对象调用类中的方法
student.classmethod()  # 调用类方法
student.method()  # 静态方法不需要参数
Student.eat(student)  # 类名.方法名  类对象调用类中的方法，需要给self赋予实例对象
print(student.name)  # 实例对象调用类中的属性
'''===========================================给实例对象动态绑定属性或者对象================================================='''
student.gender = '女'  # 给实例对象student中绑定属性
def show():
    print('定义在类之外的称为函数')

student1.show = show()  # 将函数绑定到实例对象上成为实例对象中的方法

'''===================================================封装============================================================='''
class Car:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 属性不希望在类的外部被使用，在前面添加__
    def show(self):
        print(self.name, self.__age)


stu = Car('张三',20)
stu.show()
print(stu.name)
print(dir(stu))  # 显示stu里所有属性
print(stu._Car__age)  # 在类的外部通过该方法强制访问 age
'''==================================================继承======================================================'''
class Person(object):  # 没有父类默认继承object
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name, self.age)

class Teacher(Person):  # Person是Teacher的父类，python中可以继承多个父类
    def __init__(self, name, age,teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear
    def info(self):
        super().info()  # 在子类中重写方法info，此步骤可以调用父类中的方法info
        print(self.teachofyear)


heir = Teacher('李四', '20', '28')
heir.info()  # 父类当中的方法子类可以调用
'''Object类中有一个Str()方法，用于返回对于“对象的描述”'''
class Obj:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return '我的名字是{0},今年{1}岁'.format(self.name, self.age)
obj = Obj('张三', '10')
print(obj)  # print一个实例对象默认调用对象中的__str__方法（已经在Obj中重新定义）
'''===============================================多态================================================='''
'''多态：具有多种形态，几十不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法
        在运行过程中根据变量所引用的对象类型，可以动态决定调用哪个对象中的方法'''
class Animal:
    def eat(self):
        print('动物不吃东西会饿死')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃小鱼干')
class Person:
    def eat(self):
        print('人吃五谷杂粮')


# 定义函数
def var(obj):  # 在这里创建一个对象的变量var
    obj.eat()  # 直接调用不知道那个类里的方法eat


var(Animal())  # 在这里所有的类未被实例化，直接调用函数，通过Animal()的形式直接完成类对象的实例化
var(Cat())
var(Dog())
var(Person())  # 不存在继承关系，但是Person有eat方法，也可以调用（动态语言所特有）
'''静态语言想要实现多态，必须满足
1.继承关系
2.方法重新
3.父类引用指向子类对象
   动态语言只认定类中是否存在该属性、方法'''
print(student.__dict__)  # 实例对象的属性字典
print(Student.__dict__)  # 类对象的字典中有属性和方法
print(student.__class__)
print(Student.__base__)  # 显示Student父类的第一个
print(Student.__bases__)  # 显示Student父类们（可以多个）
print(Student.__mro__)  # 显示类的层次结构
print(Student.__subclasses__())  # 显示Student的子类们

class Special:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):
        return self.name + other.name
    def __len__(self):
        return  len(self.name)

sp = Special('张三')
sp1 = Special('李四')
s = sp + sp1  # 实现了两个对象的加法运算（因为在Special类中比较暗写了__add__()方法）
# python中两个变量 c = a + b的操作正是object类中__add__()方法的实例化
print(sp.__len__())
'''=================================__new__()和__init__()================================'''
class People(object):
    def __new__(cls, *args, **kwargs):
        print('此时调用了__new__()方法，cls的id为{0}'.format(id(cls)))  # 2713490398336
        obj = super().__new__(cls)  # 重写object类中的__new__()方法，此时利用该方法创建一个实例对象obj
        print('创建的obj对象的id为{0}'.format(id(cls)))  # 2713490398336
        return obj
    def __init__(self):  # self会自动接收__new__()中的return值
        print('此时调用了__init__()方法，id为{0}'.format(id(self)))  # 2713514628576


print('Object这个类对象的id为{0}'.format(id(object)))  # 140715476896592
print('People这个类对象的id为{0}'.format(id(Person)))  # 2713490420048
people = People()
print('people这个实例对象的id为{0}'.format(id(people)))  # 2713514628576

'''===================================浅拷贝与深拷贝==========================================='''
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk
# (1) 变量的赋值
cpu1 = CPU()  # 把CPU的实例对象赋值给变量cpu1
cpu2 = cpu1  # 把变量cpu1指向的实例对象赋给变量cpu2
print(cpu1)
print(cpu2) # cpu1创建实例对象，将值赋给cpu2，两个变量指向同一个实例对象内存地址相同，实例对象指向类对象CPU()
# (2) 类的浅拷贝
disk = Disk() # 创建一个硬盘类对象
computer = Computer(cpu1, disk) # 创建一个计算机类的对象
# Computer类对象的示例对象computer中包含两个属性，分别指向CPU和Disk类对象的实例对象cpu1和disk
import copy
computer2 = copy.copy(computer)
print(computer, computer.disk, computer.cpu)
print(computer2, computer2.disk, computer2.cpu)
# 在使用浅拷贝创建Computer类的实例对象computer2时，只有被拷贝的对象会重新赋予内存空间，其子对象cpu1和disk依旧指向原实例对象
# 源对象和拷贝对象都会使用一个子对象，原对象和拷贝对象的id不同，但是子对象的id相同
# (3) 类的深拷贝
computer3 = copy.deepcopy(computer)
print(computer, computer.disk, computer.cpu)
print(computer3, computer3.disk, computer3.cpu)
# 在使用深拷贝的创建Computer类的实例对象computer3时，所有对象都会呗重新赋予内存空间，源对象和其子对象都会被重新创建实例对象

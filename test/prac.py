'''a = 1
b = 0
while a<=100 :
    if int(a%2) :
        b+=a
    a+=1
print(b)'''

'''for i in range(100,1000) :
    g = i%10
    s1 = i%100 - g
    s = s1/10
    h = (i-s1-g)/100
    if i == g**3+s**3+h**3 :
        print(i)'''

# for i in range(1,10):
#     for j in range(1,10): # for j in range(1,i+1)
#         if j<=i:
#             print(str(j)+"×"+str(i)+'='+str(i*j),end='\t')
#     print()
# name = '张三'
# age = 10
# pi = 3.1415926
# print('我叫{0}，今年{1}岁，我真的叫{0}'.format(name,age))
# print('我叫%s，今年%d岁'% (name,age))
# print(f'我叫{name},今年{age}岁')
# print('{0:.3}'.format(pi))
# print('{0:.3f'.format(pi))

lst = []
def array(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        sums = array(n-1) + array(n-2)
        # lst.append(sums)
        return sums
for i in range(1,7):
    print(array(i), end='\t')

# for i in range(3):
#     uname = input('qingshuruyonghuming')
#     pwd = input('请输入密码')
#     if uname == 'admin' and pwd == 'admin':
#         print("登陆成功")
#         break
#     else:
#         print('密码错误')
# else:
#     print("三次密码均输入错误")
'''try:
    am = int(input('请输入第一个数'))
    an = int(input('请输入第二个数'))
    result = am / an
except BaseException as e:
    print("出错了", e)
else:
    print("结果为：", result)'''
class Student:  # Student即为类名，可以由多个单词组成，每个单词首字母大写，其余小写
    native_place = '吉林'  # 直接写在类里的变量成为类属性

    # 初始化方法
    def __init__(self,name,age):
        self.name=name  # self.name称为实例属性，进行赋值操作，将局部变量name的值赋给实体属性
        self.age=age
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
student.eat()  # 对象名.方法名  调用对象的方法
Student.eat(student)  # 类名.方法名  调用类中的方法，需要给self赋予实例对象
student.native_place = '天津'
print(student.native_place)
print(student1.native_place)
class Car:
    def __init__(self,name,age):
        self.name = name
        self.__age = age  # 属性不希望在类的外部被使用，在前面添加__
    def show(self):
        print(self.name,self.__age)


stu = Car('张三',20)
stu.show()
print(stu.name)
print(dir(stu))  # 显示stu里所有属性
print(stu._Car__age)  # 在类的外部通过该方法强制访问 age

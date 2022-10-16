import math  # 关于数学运算的模块
print(id(math), type(math), math)
print(math.pi)
print(dir(math))
print(math.pow(2, 3))  # 计算2的3次方
print(math.ceil(9.001), math.floor(9.999))  # 向上取证/向下取整


from math import pi  # 只导入math中的pi
print(pi)

import subsubtest  # 导入自定义模块

from subsubtest import useless2  # 导入自定义模块中的函数或者方法
subsubtest.useless()
useless2()

def add(a, b):
    return a+b
if __name__ == '__main__':
    print(add(10, 20))  # 只有当单独运行该文件时，才会执行该语句，如果该文件作为模块被调用，则不执行
'''=================================python中的包========================================'''
# 包当中会包含__init__.py 文件
import package.module1 as ma  # 导入package包中的模块,ma是这个模块的别名
from package import module1
# 使用import只能导入包或者模块，而使用from可以导入包、模块和函数
'''=================================文件的读写操作======================================'''
# 读取文件中的内容
file = open('text.txt', 'r')
print(file.readlines())
print(file.readline(1))
file.close()
# 向文件中写内容
file = open('a.txt', 'w')
file.write('hello world')
file.close()
# 在原有内容后面进行追加
file = open('b.txt', 'a')
file.write('python')
file.close()
# mp3、jpg、doc等文件用字节进行储存，无法用记事本打开
scr_file = open('D:\\videos\Captures\Fortnite\蓝单喷三杀1.mp4', 'rb')
target_file = open("copyvideo.mp4", 'wb')
target_file.write(scr_file.read())  # 文件的拷贝操作
target_file.close()
scr_file.close()
# a+ b+ 可以让文件用读写方式打开
'''=================================上下文管理器(with方法)====================================='''
# MyContextMgr实现了特殊方法__enter__(),__exit__()称为该类对象遵守了上下文管理器协议
# 该类对象的实例对象，称为上下文管理器
class MyContextMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用了')

with MyContextMgr() as file:  # 相当于file = MyContextMgr
    file.show()  # 上下文管理器在执行方法的时候会自动调用__enter__()和__exit__()方法
'''===============================操作系统模块================================================'''
import os
os.system('notepad.exe')
os.system('calc.exe')
# 直接调用可执行文件
os.startfile(r'D:\videos\Captures\Fortnite\蓝单喷三杀1.mp4')
print(os.getcwd())  # 返回当前的工作目录
lst = os.listdir('../test')  # 获取指定路径下文件和目录信息（一个"."表示向上一级目录）
os.chdir(r'C:\Users\Administrator\Desktop\cpp\test')  # 将工作目录转移到指定路径
import os.path
print(os.path.abspath('subtest2.py'))  # 获取绝对路径
print(os.path.exists('subtest2.py'))  # 判断文件是否存在


print("hello world")
fp = open('./text.txt','a+')
print("hello world",file=fp)
fp.close()
# /t是将本制表位空出来，在下一个制表位继续输出字符
# 在字符串前面加r或者R，可以抑制转义字符作用效果
print(r'hello/nworld')
# 最后一个字符不能是'/'，要想打'/'要用转义符'//'
'''-------------------------------------数据类型及转换---------------------------------------------------'''
import keyword
print(keyword.kwlist)
# import decimal 浮点数计算
# type(bool)的True和False可以作为int的1和0
fint = 0
ffloat= 41.45
fstr = '79.468'
fstr2 = '645'
print('我叫'+str(fint)+'我敢吃')
print(float(fstr),int(ffloat),int(fstr2),type(fstr),type(ffloat),type(fstr2))
# str只有整数字符串才能转换为int类型数据，其它不能转换为int类型数据
'''---------------------------------------运算与运算符----------------------------------------------------'''
'''算术运算'''
print(11/5) # 除法运算
print(11//5) # 除法取整运算，一正一负向下取整
print(2**3) # 2的3次方
print(11%2) # 一正一负，余数=被除数-除数*商
'''位运算'''
print(4&8) # 按位与
print(4|8) # 按位或
print(4<<1) # 左移一位，高位溢出低位补零（*2）
print(4>>1) # 右移一位，高位补零低位截断（/2）
# 解包赋值可以交换
a, b, c = 10, 20, 30
print(a, b, c)
a, b, c = c, a, b
print(a, b, c)
# ‘==和!=’比较的是value，'is和is not‘比较的是id
lst1=[1,2,3,4]
lst2=[1,2,3,4]
a1=10
b1=10
a2 = b2 =10
# 不同变量名、相同的变量值用相同id，不同变量名、相同的列表元素不用相同id
'''
运算符优先级：算术>位>比较>布尔>赋值
'''
'''----------------------------------------------------------------------------------------------------'''
if a != 2:
    print("False")
elif a == 3:
    print("3")
else:
    print("啥也不是")
# python中可以用  90<=a<=100
'''==================================range()的用法======================================================='''
r = range(10)
print(r)
r = range(10,30)
print(r) # 直接print输出是 range(10,30)
print(list(r))
r = range(10,30,3) # 其中第三个元素代表输出间隔，只能用int类型数据
print(list(r))
print(9 in r)
print(30 not in r) # 用in和not in判断列表中元素存在与否，print为bool类型
print(list(range(1,10,2)))
'''=================================for_in循环============================================================'''
for item in "Python" :
    print(item)
# for_in 用于遍历字符串、列表元素
for _ in range(5) : # 不用自定义变量用"_"代替
    print("我想吃饭")
'''====================================列表list()============================================================='''
lst3 = ['string','猪肉炖粉条',56,43.485]
lst4 = list(['hello world','cunt','sucker'])
print(lst4.index("hello world")) # 列表中存在多个相同元素只返回第一个元素的索引
print(lst3.index("猪肉炖粉条",1,4)) # 范围查找，范围为[1,4)
print(lst3[0]) # 正向索引
print(lst3[-3]) # 逆向索引
lst5 = lst3[1:3:1]
print(id(lst3),id(lst5))
# 列表切片：格式[start:stop:step]，复制原列表的元素，生成新列表（不同id）
# 默认start为0，stop为最后一个元素，step为1
# step为负数是反向查询，切片列表倒序，start>stop
lst3.append(100) # 在列表末尾添加一个元素，添加lst也作为一个元素添加
lst3.extend(lst4) # 在列表末尾一次性添加多个元素
lst3.insert(1,"sdtec") # 在列表的任意位置添加一个元素
print(lst3,id(lst3))
lst3[2:3:] = lst2
# 使用切片方式完成列表任意位置的元素替换
# [start::] 将指定索引位置后所有列表元素替换
# [start:stop:] 将索引范围内的列表元素替换
print(lst3,id(lst3)) # 不生成新列表，id还是lst3的id
lst3.remove(100) # 从列表中移除一个元素，有重复元素只移除第一个
lst3.pop(3) # 根据索引移除元素，默认移除末尾元素
print(lst3,id(lst3))
lst3[1:3] = [] # 使用切片方式完成列表元素的删除
print(lst3,id(lst3)) # 不生成新列表，id还是lst3的id
lst3.clear() # 清除列表中所有元素
del lst3 # 删除列表
new_list = [10,30,20,60,80,50,40,70,90]
new_list.sort(reverse=False) # 默认为升序排序
sorted(new_list,reverse=True) # 创建新列表，对元素进行排序
lst = [i*i for i in range(1,10)] # 列表生成式
print(lst)
'''=======================================字典dict()====================================================='''
score = {'张三':398,'李四':233} # 用空花括号创建空字典
student = dict(name='jake',age=20)
# 返回key对应的value
print(score['张三']) # 不存在元素返回key error
print(score.get('张三')) # 不存在元素返回None，或者返回get('王五',23)中的23
del score['张三'] # 删除指定键值对
score.clear() # 删除字典所有元素
score['陈留'] = 100 # 添加新键值对
score['陈留'] = 234 # 改变value
keys = score.keys() # 获取字典的key
values = score.values() # 获取字典的value
items = score.items() # 获取字典的键值对，数据类型为tuple
# 字典中key不能重复，value可以重复
'''========================================元组tuple========================================================'''
# 不可变序列：字符串，元组   不能做元素的增删改操作，地址会发生变化
# 元组的创建方式
t = ('Python','world') # 直接用括号
t2 = (12,)# 元组只有一个元素时必须加'()'和','
t1 = tuple(('Python','world'))
# 空元组
t3 = ()
t4 = tuple()
'''=====================================集合================================================================'''
# 集合是没有value的字典
s = {2,3,4,5,6,7} # 集合元素不能重复
s1 = set([2,3,5,6,7,9,8]) # 集合中的元素是无序的
# 定义空集合
s2 = set()
s.add(234) # 在集合中新增一个元素
s.update({234,546,745}) # 在集合中添加多个元素
s.update([23,53,645])
s.remove(51) # 一次删除一个元素，不存在则Keyerror
s.discard(49) # 一次删除一个元素，不存在不异常
s.pop() # 一次删除一个任意元素
print(s1 == s2) # 判断两个集合是否相等  False
print(s1.issubset(s2)) # s1是否s2的子集 False
print(s1.issuperset(s2)) # s1是否s2的超集 False
print(s1.isdisjoint(s2)) # s1与s2是否含有交集，有交集是False，无交集是True
# 交集操作
print(s1.intersection(s2))
print(s1 & s2)
# 并集操作
print(s1.union(s2))
print(s1 | s2)
# 差集操作
print(s1.difference(s2)) # 在s1中减去s1与s2的交集
print(s1 - s2)
# 对称差集
print(s1.symmetric_difference(s2)) # 两个集合中不是交集的部分
print(s1 ^ s2)
S = {i for i in range(6)}  # 集合生成式
'''===============================字符串=================================================='''
name = '张三'
age = 10
pi = 3.1415926
print('我叫{0}，今年{1}岁，我真的叫{0}', format(name, age))
print('我叫%s，今年%d岁', format(name, age))
print(f'我叫{name},今年{age}岁')
print('{0:.3}'.format(pi)) #保留三位有效数字
print('{0:.3f'.format(pi)) #保留三位小数
# 字符串的编码与解码
poem = '天涯共此时'
print(poem.encode(encoding='GBK'))
print(poem.encode(encoding='UTF-8'))
byte = poem.encode(encoding='GBK')
print(byte.decode(encoding='UTF-8'))
'''=============================异常处理机制====================================='''
try:
    am = int(input('请输入第一个数'))
    an = int(input('请输入第二个数'))
    result = am / an
except BaseException as e:  # 将报错的情况用以下执行代替，BaseException总体包括报错类型
    print("出错了", e)
else:
    print("结果为：", result)
finally:
    print("finally无论程序是否异常，最后都要执行它")

import traceback  # 导入traceback模组用于报错信息打印
try:
    print('====================')
    print(23/0)
except:
    traceback.print_exc()

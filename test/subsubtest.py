# a = bool(input("输入第一个整数："))
# a = False
# b = input("输入第二个整数：")

'''if a<b :
    # print("a小")
    pass
elif a==b :
    print("a大")
else:
    print("相等")
    print(a,"你吗的",b)
    print(a+"你吗的"+b)
'''
# if a :
#     print(a,bool(a),bool(False))
# else:
#     print(bool(a))
r = range(10, 30, 5)
print(list(r))
lst2 = ["猪肉炖粉条",239,2394.34,"string",False]
lst3 = ["老妈扒茄条","旺仔牛奶"]
# lst2.extend(lst3)
lst2.extend([389,234.23,'老干妈加饭'])
print(lst2)
lst2.extend(lst3) # 在列表末尾一次性添加多个元素
lst2.insert(1, "sdtec") #在列表的任意位置添加一个元素
lst2[3:] = lst3
print(lst2)

def useless():
    pass
def useless2():
    pass
def add(a, b):
    return a+b
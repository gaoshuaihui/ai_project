# #
# def test1(a,b):
#     if a > b:
#         return "大"
#     else:
#         return "小"
#
# print(test1(10,20))
#
#
#
# print(test1(b= 10,a = 20))
#
#
# def test2(a,b = 30):
#     if a > b:
#         return "大"
#     else:
#         return "小"
#
# print(test2(10))
#
#
# def test3(a =3 , b = 3):
#     if a > b:
#         return "大"
#     else:
#         return "小"
#
# print(test3(10, 4))
# print(test3(4,b = 30))
# print(test3(b = 10, a = 4))
#
#
#
# def test4(a=3, b=3):
#     return a > b
# print( test4(10, 4) )
#
#
#
# def test5(a=3, b=3):
#     if a > b:
#         print("大")
#     else:
#         print("小")
#
#
# print( test5(10, 4) )

# 全局变量

pig = "猪猪侠"

def test6():
    pig = "小猪佩奇"
    cat = "汤姆"
    print(pig + "和" + cat)


test6()

print(pig)


super = lambda a,b: a > b
print(super(b = 10, a = 20))


list1 = [("张三",80), ("李四",90), ("王五",70), ("赵六",60)]
list1.sort(key=lambda x: x[1])
print(list1)

list2 = []





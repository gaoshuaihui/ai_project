# # 顺序结构
#
# print("第一步")
# a=10
# b = 20
# c = a+ b
# print("c的值为：", c)
#
#
# # 选择结构
# # if 语句
# if (a > b):
#     print("a大于b")
# else:
#     print("a小于等于b")
#
# # if - elif - else 语句
# if(a == b):
#     print("a和b相等")
# elif(a < b):
#     print("a小于b")
# else:
#     print("a大于b")
#
# source = 90
# if(source >= 90):
#     print("优秀")
# elif(source >= 80):
#     print("良好")
# elif(source >= 70):
#     print("一般")
# else:
#     print("不合格")

# 循环结构
# for 循环
# 打印5次hello world
for i in range(5):
    print("Hello World!")

print("-----------------")
#
list1 = ["apple","banana", "orange"]
for i in list1:
    print(i)

i = 0
while i < 5:
    print("Hello World")
    print(f"第{i}次执行")
    print(i)
    i += 1

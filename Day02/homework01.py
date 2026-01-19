# 编写一个函数，接收圆的半径作为参数，计算并返回圆的面积。

def circle_area(r):
    import math
    if r > 0 : return r * r * math.pi

# 测试
print(circle_area(2))


# 编写一个函数，接收一个年份作为参数，判断该年份是否为闰年，并返回布尔值。
def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False

# 测试
print(is_leap_year(2000))


# 编写一个程序，将列表 [1, 2, 3, 4, 5] 中的数字写入到文件 numbers.txt 中，每个数字占一行。
with open('C:\\Users\\admin\\Desktop\\numbers.txt', 'w') as f:
    for i in range(1, 9):
        f.write(str(i) + '\n')

# 编写一个程序，从文件 numbers.txt 中读取数字，计算它们的平均值并打印出来。
with open('C:\\Users\\admin\\Desktop\\numbers.txt', 'r') as f:
    sum = 0
    count = 0
    for line in f:
        num = int(line.strip())
        sum += num
        count += 1
    avg = sum / count
    print("Average:", avg)

# 调用随机密码的模块
from password_generator import generate_password
# 生成长度为8的随机密码
password = generate_password(8)
print(password)



import random

print(random.randint(1, 4))


def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 ==0):
        print("闰年")
    else:
        print("平年")

if __name__ == '__main__':
    year = int(input("你想判断的年份"))
    leap_year(year)
# 创建一个自定义模块 password_generator.py，生成指定长度的随机密码（含大小写字母和数字）
import random
import string


def generate_password(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == '__main__':
    pass
    print(string.ascii_letters + string.digits)

class Dog:
    species = "Canis lupus"  # 类属性
    dogs_count = 0  # 记录创建的狗的数量

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.dogs_count += 1  # 每创建一个实例，计数加1

    # 实例方法
    def bark(self):
        return f"{self.name} is barking!"

    # 类方法 - 使用 @classmethod 装饰器
    @classmethod
    def get_species(cls):
        """返回狗的物种"""
        return cls.species

    @classmethod
    def get_dogs_count(cls):
        """返回已创建的狗的数量"""
        return cls.dogs_count

    @classmethod
    def create_puppy(cls, name):
        """类方法作为替代构造函数，创建年龄为1岁的幼犬"""
        return cls(name, 1)


# 创建狗实例
my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.age)

# 调用类方法
print(Dog.get_species())  # 输出: Canis lupus
print(Dog.get_dogs_count())  # 输出: 1

# 使用类方法创建幼犬
puppy = Dog.create_puppy("Max")
print(f"{puppy.name} is {puppy.age} years old")  # 输出: Max is 1 years old
print(Dog.get_dogs_count())  # 输出: 2


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


result = Calculator.add(5, 3)
print(result)


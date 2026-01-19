# 练习2：创建 Shape 抽象基类及 Rectangle 子类
from abc import ABC, abstractmethod


class Shape(ABC):
    """形状抽象基类"""

    @abstractmethod
    def area(self):
        """计算面积的抽象方法"""
        pass


class Rectangle(Shape):
    """矩形类，继承自 Shape"""

    def __init__(self, width, height):
        """
        初始化矩形
        :param width: 宽度
        :param height: 高度
        """
        self.width = width
        self.height = height

    def area(self):
        """
        重写 area 方法，计算矩形面积
        :return: 面积值
        """
        return self.width * self.height


# 使用示例
if __name__ == "__main__":
    # 练习2：测试 Rectangle 类
    rectangle = Rectangle(4, 6)
    print(f"\n宽为 {rectangle.width}，高为 {rectangle.height} 的矩形:")
    print(f"面积: {rectangle.area()}")
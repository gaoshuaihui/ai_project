import math


class Circle:
    """圆形类"""

    def __init__(self, radius):
        """
        初始化圆形
        :param radius: 半径
        """
        self.radius = radius

    def area(self):
        """
        计算圆的面积
        :return: 面积值
        """
        return math.pi * self.radius ** 2

    def circumference(self):
        """
        计算圆的周长
        :return: 周长值
        """
        return 2 * math.pi * self.radius


# 使用示例
if __name__ == "__main__":
    # 练习1：测试 Circle 类
    circle = Circle(5)
    print(f"半径为 {circle.radius} 的圆:")
    print(f"面积: {circle.area():.2f}")
    print(f"周长: {circle.circumference():.2f}")
class Student:
    """学生类，存储单个学生的信息"""

    def __init__(self, name, age, grade):
        """
        初始化学生对象
        :param name: 学生姓名
        :param age: 学生年龄
        :param grade: 学生成绩
        """
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        """显示学生信息"""
        return f"姓名: {self.name}, 年龄: {self.age}, 成绩: {self.grade}"


class StudentManager:
    """学生管理器类，管理学生集合"""

    def __init__(self):
        """初始化学生管理器，创建空的学生列表"""
        self.students = []

    def add(self, student):
        """
        添加学生到管理器中
        :param student: Student 对象
        """
        self.students.append(student)
        print(f"已添加学生: {student.name}")

    def display_all(self):
        """显示所有学生的信息"""
        if not self.students:
            print("暂无学生信息")
            return

        print("\n=== 所有学生信息 ===")
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student.display_info()}")


# 使用示例
if __name__ == "__main__":
    # 创建学生管理器
    manager = StudentManager()
    # 添加学生信息
    student1 = Student("张三", 18, 85)
    student2 = Student("李四", 19, 92)
    student3 = Student("王五", 17, 78)
    manager.add(student1)
    manager.add(student2)
    manager.add(student3)
    # 显示所有学生信息
    manager.display_all()

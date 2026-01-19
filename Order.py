import random


def random_select_students(student_weights, select_num=1):
    """
    带权重随机抽取学生
    Args:
        student_weights (dict): 学生姓名为键，权重值为值的字典
        select_num (int): 要抽取的学生数量，默认抽1人

    Returns:
        list: 抽取的学生名单
    """
    # 参数校验
    if not student_weights:
        raise ValueError("学生名单不能为空！")
    if select_num < 1 or select_num > len(student_weights):
        raise ValueError(f"抽取人数需在1-{len(student_weights)}之间")

    # 拆分学生名单和对应权重
    students = list(student_weights.keys())
    weights = list(student_weights.values())

    # 带权重随机抽取（replace=False表示不重复抽取）
    selected = random.choices(students, weights=weights, k=select_num)

    return selected


# ===================== 核心配置区 =====================
student_dict = {
    "郝雅棋": 2,
    "潘玉": 2,
    "王晓端": 2,
    "张帅": 2,
    "程圣乔": 2,
    "刘盼盼": 2,
    "宋健甫": 2
}
# 要抽取的人数
select_count = 1
# ======================================================

# 执行抽取并输出结果
if __name__ == "__main__":
    try:
        result = random_select_students(student_dict, select_count)
        if select_count == 1:
            print(f"本次随机抽取的学生是：{result[0]}")
        else:
            print(f"本次随机抽取的{select_count}名学生是：{', '.join(result)}")
    except ValueError as e:
        print(f"错误：{e}")
import pymysql

def main():
    # 1.建立链接
    conn = pymysql.connect(
        host='localhost', # 数据库地址
        user='root', # 用户名
        password='123456', # 密码
        database='test2', # 数据库名
        charset='utf8', # 编码格式
    )

    # 2.创建游标对象
    cursor =conn.cursor()
    print("数据库连接成功")

    # # 3.创建学生表
    # create_table = f"""
    #     create table test2.student(
    #         id int primary key auto_increment comment '自增主键',
    #         name varchar(20) not null comment '姓名',
    #         age int not null comment '年龄',
    #         gender varchar(20) not null comment '性别：男/女'
    #     );
    # """
    #
    # # 4.执行创建表操作
    # cursor.execute(create_table)


    # 5.插入单条数据


    # insert_sql = f"""
    #     insert into student (name,age,gender) values ( %s, %s, %s)
    # """
    # data = ('张三', 19, '男')
    # cursor.execute(insert_sql, data)


    # 6.插入多条数据
    insert_sql = f"""
            insert into student (name,age,gender) values ( %s, %s, %s)
        """
    data = [
        ('李四',20,'男'),
        ('小红',23,'女'),
        ('小白',24,'女'),
        ('李帅',21,'男'),
        ('精神可嘉',25,'男'),
        ('小绿',26,'女'),
        ('小紫',18,'女'),
        ('是的',19,'男'),
        ('手打',20,'男'),
        ('李1',22,'女'),
        ('李2',20,'女'),
        ('李3',28,'女'),
        ('计算机数控',20,'男'),
    ]
    # # 批量插入
    # # 封装好的方法

    # cursor.executemany(insert_sql, data)

    for i in range(5):
        data = ('张三', i, '男')
        cursor.execute(insert_sql, data)
    # # 循环插入
    # for i in data :
    #     cursor.execute(insert_sql, i)

    conn.commit()
    conn.close()

    print("创建表成功")




if __name__ == '__main__':
    # 函数名
    main()
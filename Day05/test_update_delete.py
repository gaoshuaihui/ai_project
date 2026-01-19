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

    # # 3.执行更新操作
    # # 将女生改为girl
    # update_sql = f"""update student set gender ='girl' where gender ='女'"""
    # cursor.execute(update_sql)

    # 开启事务
    # conn.begin()

    # 4.删除操作
    delete_sql = f"""delete from student where id = 3 """
    cursor.execute(delete_sql)
    # conn.rollback()

    # conn.commit()
    print(f"受影响的行数：{cursor.rowcount}")

    conn.rollback()
    print(f"受影响的行数2：{cursor.rowcount}")

    conn.close()
    # 5.关闭链接

    print("创建表成功")




if __name__ == '__main__':
    # 函数名
    main()
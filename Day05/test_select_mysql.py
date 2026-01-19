import pymysql

def main():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='test2')
    cursor = db.cursor()

    select_sql = 'select * from test2.student where age > 25'
#     select_sql = f"""
#         select
#             age,gender,count(*) as age_cnt
#         from test2.student
#         group by age,gender
#         order by age desc,age_cnt desc;
# """
    cursor.execute(select_sql)

    # cursor.execute('select * from test2.student limit 5')

    # 获取所有结果
    # data = cursor.fetchall()

    # # 获取第一条结果
    # data = cursor.fetchone()

    # 获取指定数量的结果
    data = cursor.fetchmany(size=5)

    print(data)
    print(type(data))

    for i in data:
        print(i)

    db.close()

if __name__ == '__main__':
    main()
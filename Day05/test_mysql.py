import pymysql

def main():
    db = pymysql.connect(host='localhost', user='root', password='123456', database='test1')
    cursor = db.cursor()
    cursor.execute('select * from test1.students')
    data = cursor.fetchall()
    for i in data:
        print(i)
    # db.close()
    print("查询成功")
    db.close()

if __name__ == '__main__':
    main()
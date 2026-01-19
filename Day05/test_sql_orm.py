from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建数据库引擎
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test2')
charset = 'utf8'
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# 创建数据模型
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    gender = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)

# 查询年龄>25 的学生
filter_students =  session.query(Student).filter(Student.age > 25).all()

print(filter_students)

for i in filter_students:
    print(i.name, i.gender, i.age)

session.close()

# print(filter_students)



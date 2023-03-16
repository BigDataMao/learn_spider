import pymysql

# 创建连接对象
conn = pymysql.connect(
    host='124.221.228.129',
    user='root',
    password='mxw19910712@MYSQL'
)

# 用连接对象创建执行游标
cursor = conn.cursor()

# DDL语句
cursor.execute('create database spider_data;')
cursor.execute('create table test.test_pymysql(name varchar(50),age int)')

# DML语句
cursor.execute("insert into  test.test_pymysql values ('mao',18 )")
# 用连接对象提交
conn.commit()

# select语句最后获得的都是元组,可以迭代
cursor.execute("select count(1) from test.test_pymysql")
print(cursor.fetchone()[0])

# 关闭连接
conn.close()
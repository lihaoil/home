import pymysql
# 连接数据库
db = pymysql.connect('10.220.20.87','root','1q2w3e4r','wshtest')
# 创建cursor游标对象
cursor = db.cursor()
# 查询sql
cursor.execute('select * from emp')
'''
try:
    # 执行sql语句
    cursor.execute('sql')
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
'''
# 查询一条sql记录
print(cursor.fetchone())
# 查询全部sql记录
print(cursor.fetchall())
# 关闭数据库
db.close()
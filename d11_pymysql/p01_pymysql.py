from pymysql import Connection

conn=Connection(
    host="localhost",
    port=3306,
    user="root",
    passwd="123456",
    autocommit=True   #自动提交
)
#打印版本信息
print(conn.get_server_info())

#执行SQL
cursor=conn.cursor()

conn.select_db("hehe_db")


#cursor.execute("create table t_pytest(id int);")

cursor.execute("select * from lwq_student;")
res=cursor.fetchall()
print(res)

for r in res:
    print(r)



conn.close()
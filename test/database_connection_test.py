from pymysql import Connection

conn = Connection(
    host="localhost",  # 主机名
    port=3306,  # 端口
    user="root",
    password="99221",
    database="pyqt"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM vdot")
result = cursor.fetchall()

print(result)

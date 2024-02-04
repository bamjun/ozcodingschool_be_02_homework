import pymysql
import pass1

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=pass1.password(),
    db="classicmodels",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,  # 이 속성이 없을경우 튜플로 데이터 가져옴.
)


cursor = connection.cursor()
sql = "select * from customers"
cursor.execute(sql)

customers = cursor.fetchone()
print("customers : ", customers["customerNumber"])
print("customers : ", customers["customerName"])
print("customers : ", customers["country"])
print("customers : ", customers["city"])

import pymysql
import pass1

# https://visioneer.notion.site/04-Python-MySQL-PyMySQL-b622e72ab5e64bfa9e885f2dacdee46c
# 데이터베이스 연결 설정
connection = pymysql.connect(
    host="localhost",
    user="root",
    password=pass1.password(),
    db="classicmodels",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,  # 이 속성이 없을경우 튜플로 데이터 가져옴.
)


## 1. select * from
def get_customers():
    cursor = connection.cursor()
    sql = "select * from customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers : ", customers["customerNumber"])
    print("customers : ", customers["customerName"])
    print("customers : ", customers["country"])
    print("customers : ", customers["city"])

    cursor.close()


## 2. Insert into
def add_customers():
    cursor = connection.cursor()
    name = "beomjun"
    family_name = "kim"
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) values(1005, '{name}', '{family_name}')"
    cursor.execute(sql)
    connection.commit()
    cursor.close()


## 3. update set
def update_customer():
    cursor = connection.cursor()
    update_name = "update_inseop"
    contactLastName = "beomjun"

    sql = f"update customers set customerNmae='{update_name}', contact='{contactLastName}' where customerNumber=501"
    cursor.execute(sql)
    connection.commit()
    cursor.close()


## 4. delete from
def delete_customer():
    cursor = connection.cursor()
    sql = "delete from customers where customerNumber = 500"
    cursor.execute(sql)
    connection.commit()
    cursor.close()


delete_customer()

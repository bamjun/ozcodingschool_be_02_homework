import pymysql
import pass1

# https://visioneer.notion.site/04-Python-MySQL-PyMySQL-b622e72ab5e64bfa9e885f2dacdee46c
# 데이터베이스 연결 설정

import pymysql


def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            connection.commit()


def main():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password=pass1.password(),
        db="classicmodels",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,  # 이 속성이 없을경우 튜플로 데이터 가져옴.
    )
    try:
        # SELECT 연산
        result = execute_query(connection, "SELECT * FROM table_name")
        print("SELECT 연산 결과:")
        for row in result:
            print(row)

        # INSERT 연산
        execute_query(
            connection,
            "INSERT INTO table_name (column1, column2) VALUES (%s, %s)",
            ("data1", "data2"),
        )
        print("INSERT 연산 수행됨.")

        # UPDATE 연산
        execute_query(
            connection,
            "UPDATE table_name SET column1=%s WHERE column2=%s",
            ("new_data", "criteria"),
        )
        print("UPDATE 연산 수행됨.")

        # DELETE 연산
        execute_query(
            connection, "DELETE FROM table_name WHERE column_name=%s", ("criteria",)
        )
        print("DELETE 연산 수행됨.")

    finally:
        connection.close()


if __name__ == "__main__":
    main()

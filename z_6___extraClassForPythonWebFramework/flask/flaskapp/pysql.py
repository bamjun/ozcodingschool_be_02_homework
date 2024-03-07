import pymysql.cursors

connection = pymysql.connect(
    host="localhost", user="root", password="1Rlaqjawns@18", db="oz_flask2", cursorclass=pymysql.cursors.DictCursor
)

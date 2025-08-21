import pymysql

connection = pymysql.connect(host='localhost', user='root', password='ShyamAgra@230', database='khushi_db',
 port=3306, charset='utf8mb4' )

if connection:
    print('database connected')
else:
    print('Database connection failed')
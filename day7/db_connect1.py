import pymysql

def connect_db():
    try:
        conn = pymysql.Connect(host='localhost', user='root', 
        password='Root123', database='mtd_db', port=3306)
        print('Database connected')
        return conn
    except:
        print('Database connection failed')

def disconnect_db(connection):
    if connection:
        connection.close()
        print('Database disconnected')
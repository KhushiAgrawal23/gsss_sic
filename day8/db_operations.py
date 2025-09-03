# import D:\\nithin_learning\\gsss_sic\\day7\\db_connect as db
import pymysql

class Employee:
    def __init__(self, name='', designation='', phone_number=0, commission=0.0, salary=0.0, years_of_exp=0, location=''):
        self.name = name
        self.designation = designation
        self.phone_number = phone_number
        self.commission = commission
        self.salary = salary
        self.years_of_exp = years_of_exp
        self.location = location

    def __str__(self):
        total_salary = int(self.salary) + int(self.commission)
        return f'Name={self.name}, Designation={self.designation}, Total_salary={total_salary}, Location={self.location}'

class EmployeeOperations:
    def connect_db(self):
        try:
            conn = pymysql.Connect(host='localhost', user='root', 
            password='Root123', database='mtd_db', port=3306)
            print('Database connected')
            return conn
        except:
            print('Database connection failed')

    def disconnect_db(self, connection):
        if connection:
            connection.close()
            print('Database disconnected')

    def read_employee_details(self):
        name = input('Enter employee name: ')
        designation = input('Enter employee designation: ')
        phone_number = input('Enter employee phone_number: ')
        commisssion = input('Enter employee commisssion: ')
        salary = input('Enter employee salary: ')
        years_of_exp = input('Enter employee years_of_exp: ')
        location = input('Enter employee location: ')
        return (name, designation, phone_number, commisssion, salary, years_of_exp, location)

    def create_row(self):
        employee = self.read_employee_details()
        query = 'insert into employees(name, designation, phone_number, commission, salary, years_of_exp, location) values(%s, %s, %s, %s, %s, %s, %s)'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, employee)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        if count == 1:
            print('Row inserted')
        else:
            print('Row insertion failed')

    def update_row(self):
        query = 'update employees set location = %s, salary = %s where id = %s'
        salary = float(input('Enter the new salary to be updated: '))
        location = input('Enter new location of employee: ')
        id =  int(input('Enter id of employee to update details: '))
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, (location, salary, id))
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        if count == 1:
            print('Row updated')
        else:
            print('Row updation failed')

    def delete_row(self):
        id =  int(input('Enter id of employee to update details: '))
        query = f'delete from employees where id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        if count == 1:
            print('Row deleted')
        else:
            print('Row deletion failed')

    def search_row(self):
        id =  int(input('Enter the employee Id to search:'))
        query = f'select * from employees where id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            print(f'Employee details are {row}')
        else:
            print(f'Employee with Id = {id} not found')
        cursor.close()
        self.disconnect_db(connection)
        
    def list_all_rows(self):
        query = 'select * from employees'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            print('List of all Employees:')
            for row in rows:
                employee = Employee(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                print(employee)
        elif len(rows) == 0:
            print('No employee records found')
        else:
            print('Fetching all rows failed')
        cursor.close()
        self.disconnect_db(connection)

    def create_table(self):
        query = ''' create table IF NOT EXISTS employees(
        id int auto_increment primary key,
        name varchar(50) not null,
        designation	varchar(50),
        phone_number bigint	unique not null,
        commission float default(0),
        salary float check(salary >= 15000),
        years_of_exp tinyint,
        location varchar(50) );  '''
        connection = self.connect_db()
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.close()
            self.disconnect_db(connection)
        except:
            print('Table creation failed')

    def create_database(self):
        db_name = input('Enter the database name you wish to create: ')
        query = f'create database if not exists {db_name}'
        connection = self.connect_db()
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.close()
            self.disconnect_db(connection)
        except:
            print('database creation failed')
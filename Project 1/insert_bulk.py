import re

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# MySQL connection params
HOSTNAME='localhost'
DATABASE='company'
USERNAME='root'
PASSWORD='prash94@MySQL'

# file locations for bulk insert insert 
bulk_insert_location_employee='./data/EMPLOYEE.txt' 
bulk_insert_location_department='./data/DEPARTMENT.txt' 
bulk_insert_location_dept_locations='./data/DEPT_LOCATIONS.txt' 
bulk_insert_location_project='./data/PROJECT.txt' 
bulk_insert_location_works_on='./data/WORKS_ON.txt' 
bulk_insert_location_dependent='./data/DEPENDENT.txt'

def get_db_connection():
    return mysql.connector.connect(
                host=HOSTNAME,
                database=DATABASE,
                user=USERNAME,
                password=PASSWORD
            )


def get_db_cursor(db_connection):
    return db_connection.cursor()

def get_employee_query():
    return 'INSERT INTO employee(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES ( %s, %s, %s, %s, STR_TO_DATE(%s, "%d-%b-%Y"), %s, %s, %s, %s, %s);'

def get_department_query():
    return 'INSERT INTO department(Dname, Dnumber, Mgr_ssn, Mgr_start_date) VALUES ( %s, %s, %s, STR_TO_DATE(%s, "%d-%b-%Y"));'

def get_dependent_query():
    return 'INSERT INTO dependent(Essn, Dependent_name, Sex, Bdate, Relationship) VALUES ( %s, %s, %s, STR_TO_DATE(%s, "%d-%b-%Y"), %s);'

def get_dept_locations_query():
    return 'INSERT INTO dept_locations(Dnumber, Dlocation) VALUES ( %s, %s);'

def get_project_query():
    return 'INSERT INTO project(Pname, Pnumber, Plocation, Dnum) VALUES ( %s, %s, %s, %s);'

def get_works_on_query():
    return 'INSERT INTO works_on(Essn, Pno, Hours) VALUES ( %s, %s, %s);'

def bulk_insert(db_connection, db_cursor, query, data):
    print(f'Query: {query}\nData: {data}')
    try:
        db_cursor.executemany(query, data)
        db_connection.commit()
    except mysql.connector.Error as error:
        raise error

def preprocess_data(file_location, is_employee_table):
    split_char = ","
    if is_employee_table:
        split_char = ", "

    data = []
    employee_file = open(file_location, 'r') 
    lines = employee_file.readlines() 
    print(f'Number of lines: {len(lines)}')
    for line in lines:
        chars_to_replace = ["'", " ", "\r", "\n"]
        values = [ re.sub("|".join(chars_to_replace), "", value) for value in line.split(split_char) if value != '\n' ]

        if values:
            data.append(tuple(values))
        
    print(f'Number of lines in data: {len(data)}')
    print(data)
    return data

if __name__ == "__main__":
    db_connection = get_db_connection()
    db_cursor = get_db_cursor(db_connection)

    # insert data from EMPLOYEE.txt
    employee_data = preprocess_data(bulk_insert_location_employee, True)
    bulk_insert(db_connection, db_cursor, get_employee_query(), employee_data)
    
    # insert data from DEPARTMENT.txt
    department_data = preprocess_data(bulk_insert_location_department, False)
    bulk_insert(db_connection, db_cursor, get_department_query(), department_data)

    # insert data from DEPT_LOCATIONS.txt
    dept_location_data = preprocess_data(bulk_insert_location_dept_locations, False)
    bulk_insert(db_connection, db_cursor, get_dept_locations_query(), dept_location_data)


    # insert data from PROJECT.txt
    project_data = preprocess_data(bulk_insert_location_project, False)
    bulk_insert(db_connection, db_cursor, get_project_query(), project_data)


    # insert data from WORKS_ON.txt
    works_on_data = preprocess_data(bulk_insert_location_works_on, False)
    
    # allow only unique combination of (Essn, Pno) in works_on table
    # making a set out of tuple and then converting it back to list..
    works_on_data = list(set(works_on_data))
    bulk_insert(db_connection, db_cursor, get_works_on_query(), works_on_data)


     # insert data from DEPENDENT.txt
    dependent_data = preprocess_data(bulk_insert_location_dependent, False)
    bulk_insert(db_connection, db_cursor, get_dependent_query(), dependent_data)

    if db_connection.is_connected():
        db_cursor.close()
        db_connection.close()
        print("MySQL connection is closed")
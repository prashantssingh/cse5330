import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# MySQL connection params
HOSTNAME='localhost'
DATABASE='user_accounts'
USERNAME='root'
PASSWORD='prash94@MySQL'

def get_db_connection():
    return mysql.connector.connect(
                host=HOSTNAME,
                database=DATABASE,
                user=USERNAME,
                password=PASSWORD
            )

def get_db_cursor(db_connection):
    return db_connection.cursor()

def insert_into_user_accounts(db_connection, db_cursor, data):
    if data is None:
        data = [(1, "Prashant Singh", "1234567890"), 
                (2, "Krishna Rao", "1134567890"),
                (3, "John Doe", "1234563344"),
                (4, "Ben Dower", "1134692890"),
                (5, "Hugh Ash", "3344556677"),
                (6, "Jane Doe", "11223453456"),
                (7, "Glenn McGrath", "4657485734"),
                (8, "Planter Nigh", "9988776655"),
                (9, "Ginger Dickens", "1234123455"),
                (10, "Behram Khalili", "6789678900")]

    query = 'INSERT INTO user_accounts(id, username, phonenumber) VALUES (%s, %s, %s);'
    bulk_insert(db_connection, db_cursor, query, data)
    print(f"Inserted {len(data)} new accounts..")

def insert_into_roles(db_connection, db_cursor, data):
    if data is None:
        data = [(1, "Admin", "User-role name: Admin"), 
                (2, "Regular User", "User-role name: Regular User"),
                (3, "Guest", "User-role name: Guest")] 

    query = 'INSERT INTO roles(id, rolename, description) VALUES (%s, %s, %s);'
    bulk_insert(db_connection, db_cursor, query, data)
    print(f"Inserted {len(data)} new roles..")

def insert_into_tables(db_connection, db_cursor, data):
    if data is None:
        data = [(1, "Table 1"),
                (2, "Table 2"),
                (3, "Table 3"),
                (4, "Table 4"),
                (5, "Table 5"),
                (6, "Table 6"),
                (7, "Table 7"),
                (8, "Table 8"),
                (9, "Table 9"),
                (10, "Table 10")]

    query = 'INSERT INTO tables(id, tablename) VALUES (%s, %s);'
    bulk_insert(db_connection, db_cursor, query, data)
    print(f"Inserted {len(data)} new tables..")

def insert_into_privileges(db_connection, db_cursor, data):
    if data is None:
        data = [(1, 1, 1, 1, 1),
                (2, 1, 1, 0, 0),
                (3, 1, 0, 0, 0)]

    query = 'INSERT INTO privileges(id, select_privileges, update_privileges, delete_privileges, create_privileges) VALUES (%s, %s, %s, %s, %s);'
    bulk_insert(db_connection, db_cursor, query, data)
    print(f"Inserted {len(data)} new privileges..")

def insert_into_user_roles_mapping(db_connection, db_cursor, data):
    if data is None:
        data = [(1, 1, 1),
                (2, 1, 2),
                (3, 1, 3),
                (4, 2, 4),
                (5, 2, 5),
                (6, 2, 6),
                (7, 3, 7),
                (8, 3, 8),
                (9, 3, 9),
                (10, 3, 10)]

    query = 'INSERT INTO user_roles_mapping(id, roleid, userid) VALUES (%s, %s, %s);'
    bulk_insert(db_connection, db_cursor, query, data)
    print(f"Inserted {len(data)} mappings for Relation (USER_ACCOUNT, ROLE)..")

def insert_into_privileges_roles_mapping(db_connection, db_cursor, data):
    if data is None:
        data = [(1, 1, 1),
                (2, 2, 2),
                (3, 3, 3)]

    query = 'INSERT INTO privileges_roles_mapping(id, roleid, privilegeid) VALUES (%s, %s, %s);'
    bulk_insert(db_connection, db_cursor, query, data)
    print(f"Inserted {len(data)} mappings for Relation (ACCOUNT_PRIVILEGES, ROLE)..")

def insert_into_privileges_roles_tables_mapping(db_connection, db_cursor, data):
    if data is None:
        data = [(1, 1, 1, 1),
                (2, 1, 1, 2),
                (3, 1, 1, 3),
                (4, 2, 2, 4),
                (5, 2, 2, 5),
                (6, 2, 2, 6),
                (7, 3, 3, 7),
                (8, 3, 3, 8),
                (9, 3, 3, 9),
                (10, 3, 3, 10)]

    query = 'INSERT INTO privileges_roles_tables_mapping(id, roleid, privilegeid, tableid) VALUES (%s, %s, %s, %s);'
    bulk_insert(db_connection, db_cursor, query, data)
    print(f"Inserted {len(data)} mappings for Relation (RELATION_PRIVILEGE, ROLE, and TABLE)..")

def hybrid_options():
    return '''
1. Get PRIVILEGES by ROLE_ID
2. Get PRIVILEGES by USER_ACCOUNT
3. Check for a PRIVILEGE available (granted) to a particular USER_ACCOUNT
>>> Enter your option: '''

def display_options():
    return '''
1. Insert a new USER_ACCOUNT
2. Insert a new ROLE
3. Insert a new TABLE
4. Insert a new PRIVILEGE
5. Relate a USER_ACCOUNT to a ROLE
6. Relate an ACCOUNT_PRIVILEGE to a ROLE
7. Relate a RELATION_PRIVILEGE, ROLE, and TABLE
8. Check Privileges using ROLE_ID or USER_ID
>>> Enter your option: '''

def process_options(option):
    if option == 1:
        print("Enter comma-separated values for new USER_ACCOUNT (id, username, phonenumber): ")
        values = input().split(",")
        if len(values) != 3: print("Invalid data for new account")
        insert_into_user_accounts(db_connection, db_cursor, [tuple(values)])

    if option == 2:
        print("Enter comma-separated values for new ROLE (id, rolename, description): ")
        values = input().split(",")
        if len(values) != 3: print("Invalid data for new ROLE")
        insert_into_roles(db_connection, db_cursor, [tuple(values)])

    if option == 3:
        print("Enter comma-separated values for new PRIVILEGES (id, select_privileges, update_privileges, delete_privileges, create_privileges): ")
        values = input().split(",")
        if len(values) != 5: print("Invalid data for new PRIVILEGES")
        insert_into_privileges(db_connection, db_cursor, [tuple(values)])

    if option == 4:
        print("Enter comma-separated values for new TABLE (id, tablename): ")
        values = input().split(",")
        if len(values) != 2: print("Invalid data for new TABLE")
        insert_into_tables(db_connection, db_cursor, [tuple(values)])

    if option == 5:
        print("Enter comma-separated values for new relation of USER_ACCOUNT to a ROLE (id, roleid, userid): ")
        values = input().split(",")
        if len(values) != 3: print("Invalid data for new relation of USER_ACCOUNT to a ROLE")
        insert_into_user_roles_mapping(db_connection, db_cursor, [tuple(values)])
        
    if option == 6:
        print("Enter comma-separated values for new relation of PRIVILEGES to a ROLE (id, roleid, privilegeid): ")
        values = input().split(",")
        if len(values) != 3: print("Invalid data for new relation of PRIVILEGES to a ROLE")
        insert_into_privileges_roles_mapping(db_connection, db_cursor, [tuple(values)])

    if option == 7:
        print("Enter comma-separated values for new relation of RELATION_PRIVILEGE, ROLE, and TABLE (id, roleid, privilegeid, tableid): ")
        values = input().split(",")
        if len(values) != 4: print("Invalid data for new relation of RELATION_PRIVILEGE, ROLE, and TABLE")
        insert_into_privileges_roles_tables_mapping(db_connection, db_cursor, [tuple(values)])

    if option == 8:
        option = int(input(hybrid_options()))
        if option == 1:
            role_id = int(input("Enter role-id: "))
            query = f"SELECT * FROM privileges WHERE id = (SELECT privilegeid FROM privileges_roles_mapping WHERE roleid = {role_id});"
            db_cursor.execute(query)
            rows = db_cursor.fetchall()

            if not db_cursor.rowcount: print("No such record found")
            record = rows[0]
            permissions = list()
            if record[0]: permissions.append("Select")
            if record[1]: permissions.append("Update")
            if record[2]: permissions.append("Delete")
            if record[3]: permissions.append("Create")
            print(f"PRIVILEGES for role-id - {role_id}: {permissions}")

        if option == 2:
            role_id = int(input("Enter user-id: "))
            query = f"SELECT * FROM privileges WHERE id = (SELECT privilegeid FROM privileges_roles_mapping WHERE roleid = (SELECT roleid FROM user_roles_mapping WHERE userid = {role_id}));"
            db_cursor.execute(query)
            rows = db_cursor.fetchall()

            if not db_cursor.rowcount: print("No such record found")
            record = rows[0]
            permissions = list()
            if record[0]: permissions.append("Select")
            if record[1]: permissions.append("Update")
            if record[2]: permissions.append("Delete")
            if record[3]: permissions.append("Create")
            print(f"PRIVILEGES for user-id - {role_id}: {permissions}")

        if option == 3:
            role_id = int(input("Enter user-id: "))
            query = f"SELECT * FROM privileges WHERE id = (SELECT privilegeid FROM privileges_roles_mapping WHERE roleid = (SELECT roleid FROM user_roles_mapping WHERE userid = {role_id}));"
            db_cursor.execute(query)
            rows = db_cursor.fetchall()

            if not db_cursor.rowcount: print("No such record found")
            record = rows[0]
            permissions = set()
            if record[0]: permissions.add("select")
            if record[1]: permissions.add("update")
            if record[2]: permissions.add("delete")
            if record[3]: permissions.add("create")
            
            permission = input("Enter privilege you want to check: ")
            print(f"PRIVILEGE - {permission} present?: {permission.lower() in permissions}")

def run(db_connection, db_cursor):
    insert_into_user_accounts(db_connection, db_cursor, None)
    insert_into_roles(db_connection, db_cursor, None)
    insert_into_tables(db_connection, db_cursor, None)
    insert_into_privileges(db_connection, db_cursor, None)
    insert_into_user_roles_mapping(db_connection, db_cursor, None)
    insert_into_privileges_roles_mapping(db_connection, db_cursor, None)
    insert_into_privileges_roles_tables_mapping(db_connection, db_cursor, None)

    while True:
        option = int(input(display_options()))
        process_options(option)


def bulk_insert(db_connection, db_cursor, query, data):
    try:
        db_cursor.executemany(query, data)
        db_connection.commit()
    except mysql.connector.Error as error:
        raise error

if __name__ == "__main__":
    db_connection = get_db_connection()
    db_cursor = get_db_cursor(db_connection)

    run(db_connection, db_cursor)

    if db_connection.is_connected():
        db_cursor.close()
        db_connection.close()
        print("MySQL connection is closed")
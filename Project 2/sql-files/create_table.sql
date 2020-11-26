DROP DATABASE user_accounts;

SHOW DATABASES; 

CREATE DATABASE user_accounts;

USE user_accounts;

CREATE TABLE roles (
    id INT(10) NOT NULL PRIMARY KEY,
    rolename VARCHAR(255) NOT NULL UNIQUE,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE user_accounts (
    id INT(10) NOT NULL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    phonenumber VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE user_roles_mapping (
    id INT(10) NOT NULL PRIMARY KEY,
    roleid INT(10) NOT NULL,
    userid INT(10) NOT NULL,
    FOREIGN KEY (roleid) REFERENCES roles(id),
    FOREIGN KEY (userid) REFERENCES user_accounts(id)
);

CREATE TABLE privileges(
    id INT(10) NOT NULL PRIMARY KEY,
    select_privileges INT(1) NOT NULL,
    update_privileges INT(1) NOT NULL,
    delete_privileges INT(1) NOT NULL,
    create_privileges INT(1) NOT NULL
);

CREATE TABLE privileges_roles_mapping (
    id INT(10) NOT NULL PRIMARY KEY,
    roleid INT(10) NOT NULL,
    privilegeid INT(10) NOT NULL,
    FOREIGN KEY (roleid) REFERENCES roles(id),
    FOREIGN KEY (privilegeid) REFERENCES privileges(id)
);

CREATE TABLE tables (
    id INT(10) NOT NULL PRIMARY KEY,
    tablename VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE privileges_roles_tables_mapping (
    id INT(10) NOT NULL PRIMARY KEY,
    roleid INT(10) NOT NULL,
    privilegeid INT(10) NOT NULL,
    tableid INT(10) NOT NULL,
    FOREIGN KEY (roleid) REFERENCES roles(id),
    FOREIGN KEY (privilegeid) REFERENCES privileges(id),
    FOREIGN KEY (tableid) REFERENCES tables(id)
);

-- INSERT INTO USER_ROLES VALUES("Admin", "User-role name: Admin");
-- INSERT INTO USER_ROLES VALUES("Regular User", "User-role name: Regular User");
-- INSERT INTO USER_ROLES VALUES("Guest", "User-role name: Guest");

-- INSERT INTO USER_ACCOUNTS VALUES("1", "Prashant Singh", "1234567890", "Admin");
-- INSERT INTO USER_ACCOUNTS VALUES("2", "Krishna Rao", "1134567890", "Admin");
-- INSERT INTO USER_ACCOUNTS VALUES("3", "John Doe", "1234563344", "Admin");
-- INSERT INTO USER_ACCOUNTS VALUES("4", "Ben Dower", "1134692890", "Regular User");
-- INSERT INTO USER_ACCOUNTS VALUES("5", "Hugh Ash", "3344556677", "Regular User");
-- INSERT INTO USER_ACCOUNTS VALUES("6", "Jane Doe", "11223453456", "Regular User");
-- INSERT INTO USER_ACCOUNTS VALUES("7", "Glenn McGrath", "4657485734", "Guest");
-- INSERT INTO USER_ACCOUNTS VALUES("8", "Planter Nigh", "9988776655", "Guest");
-- INSERT INTO USER_ACCOUNTS VALUES("9", "Ginger Dickens", "1234123455", "Guest");
-- INSERT INTO USER_ACCOUNTS VALUES("10", "Behram Khalili", "6789678900", "Guest");

-- INSERT INTO PRIVILEGES VALUES(1, 1, 1, 1, 1, "Admin");
-- INSERT INTO PRIVILEGES VALUES(2, 1, 1, 1, 1, "Admin");
-- INSERT INTO PRIVILEGES VALUES(3, 1, 1, 1, 1, "Admin");
-- INSERT INTO PRIVILEGES VALUES(4, 1, 1, 0, 0, "Regular User");
-- INSERT INTO PRIVILEGES VALUES(5, 1, 1, 0, 0, "Regular User");
-- INSERT INTO PRIVILEGES VALUES(6, 1, 1, 0, 0, "Regular User");
-- INSERT INTO PRIVILEGES VALUES(7, 1, 0, 0, 0, "Guest");
-- INSERT INTO PRIVILEGES VALUES(8, 1, 0, 0, 0, "Guest");
-- INSERT INTO PRIVILEGES VALUES(9, 1, 0, 0, 0, "Guest");
-- INSERT INTO PRIVILEGES VALUES(1, 1, 0, 0, 0, "Guest");

-- INSERT INTO Tables VALUES("Table 1", "Admin", "1");
-- INSERT INTO Tables VALUES("Table 2", "Admin", "2");
-- INSERT INTO Tables VALUES("Table 3", "Admin", "3");
-- INSERT INTO Tables VALUES("Table 4", "Regular User", "4");
-- INSERT INTO Tables VALUES("Table 5", "Regular User", "5");
-- INSERT INTO Tables VALUES("Table 6", "Regular User", "6");
-- INSERT INTO Tables VALUES("Table 7", "Guest", "7");
-- INSERT INTO Tables VALUES("Table 8", "Guest", "8");
-- INSERT INTO Tables VALUES("Table 9", "Guest", "9");
-- INSERT INTO Tables VALUES("Table 10", "Guest", "10");

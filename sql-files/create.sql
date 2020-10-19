SHOW DATABASES;

CREATE DATABASE company;

USE company;

CREATE TABLE employee (
Fname VARCHAR(150) NOT NULL,
Minit VARCHAR(50), 
Lname VARCHAR(150) NOT NULL, 
Ssn VARCHAR(200) NOT NULL, 
Bdate DATE,
Address VARCHAR(255),
Sex VARCHAR(150),
Salary DECIMAL(10,2),
Super_ssn VARCHAR(200),
Dno INT NOT NULL,
PRIMARY KEY (Ssn));

CREATE TABLE department(
Dname VARCHAR(150) NOT NULL UNIQUE,
Dnumber INT NOT NULL,
Mgr_ssn VARCHAR(200) NOT NULL,
Mgr_start_date DATE,
PRIMARY KEY (Dnumber),
FOREIGN KEY (Mgr_ssn) REFERENCES employee(Ssn) );

CREATE TABLE dept_locations(
Dnumber INT NOT NULL,
Dlocation VARCHAR(150) NOT NULL,
PRIMARY KEY (Dnumber, Dlocation),
FOREIGN KEY (Dnumber) REFERENCES department(Dnumber) );

CREATE TABLE project(
Pname VARCHAR(150) NOT NULL UNIQUE,
Pnumber INT NOT NULL,
Plocation VARCHAR(150),
Dnum INT NOT NULL,
PRIMARY KEY (Pnumber),
FOREIGN KEY (Dnum) REFERENCES department(Dnumber) );

CREATE TABLE works_on(
Essn VARCHAR(200) NOT NULL,
Pno INT NOT NULL,
Hours DECIMAL(3,1) NOT NULL,
PRIMARY KEY (Essn, Pno),
FOREIGN KEY (Essn) REFERENCES employee(Ssn),
FOREIGN KEY (Pno) REFERENCES project(Pnumber) );

CREATE TABLE dependent(
Essn VARCHAR(200) NOT NULL,
Dependent_name VARCHAR(150) NOT NULL,
Sex VARCHAR(150),
Bdate DATE,
Relationship VARCHAR(100),
PRIMARY KEY (Essn, Dependent_name),
FOREIGN KEY (Essn) REFERENCES employee(Ssn) );

SHOW TABLES;

ALTER TABLE department DROP FOREIGN KEY department_ibfk_1;

ALTER TABLE project DROP FOREIGN KEY project_ibfk_1;

ALTER TABLE works_on DROP FOREIGN KEY works_on_ibfk_1;

ALTER TABLE works_on DROP FOREIGN KEY works_on_ibfk_2;

ALTER TABLE dependent DROP FOREIGN KEY dependent_ibfk_1;


DELETE FROM employee;
DELETE FROM department; 
DELETE FROM works_on;
DELETE FROM dept_locations;
DELETE FROM project;
DELETE FROM dependent;

SELECT * FROM employee;
SELECT * FROM department; 
SELECT * FROM works_on;
SELECT * FROM dept_locations;
SELECT * FROM project;
SELECT * FROM dependent;

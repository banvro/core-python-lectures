
use morning_clg;

show tables;

select * from teacher_backup;

-- creating a backup copy of a entire table
create table teacher_backup as select * from our_teacher;

-- copy speacific columns
create table tracher_main_info as 
select teacher_id, teacher_name, teacher_email,
teacher_contact from our_teacher;

show tables;

select * from tracher_main_info;


-- ------------------------------------
-- DDL --> CRUD
-- after table creation modify that table

create table techer as select * from tracher_main_info;

select * from techer;

-- ---> modify table

-- 1) how to add a new column in our existing table

alter table techer add column course varchar(20);

select * from techer;

-- 2) how to add multiple columns in exising table

alter table techer 
	add age int, 
	add f_name varchar(150);

select * from techer;

-- 3) how to chnage datatype of an column

alter table techer modify f_name int;

select * from techer;

-- 4) we wana change column name in exsiting table

alter table techer change teacher_email email_id varchar(120);

select * from techer;

alter table techer rename column teacher_name to t_name;

-- 5) deleteing an column from existing table..

alter table techer drop column f_name;

select * from techer;

-- 6) rename table name

rename table techer to teacher;


----------------------------------------------------
table example

show tables;

create table students(
	roll_num int auto_increment primary key,
    stu_name varchar(120),
    stu_email varchar(120),
    stu_contact varchar(12),
    age int, 
    fees int default 25,
    joining_date datetime default current_timestamp,
    subjects varchar(120)
);

select * from students;

alter table students modify column fees int default 25000;

insert into students (stu_name, stu_email, stu_contact, age, subjects)
values("Sham Lal", "sham@gmail.com", "28349234", 23, "DA");



select * from teacher;

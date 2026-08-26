
	-- this code create the table

	SHOW DATABASES;

	CREATE DATABASE morning_clg;

	drop database morning_clg;

-------------------------------------------------------------------------------------------
show databases;

-- active a database
use morning_clg;

-- check how many tables in my database
show tables;

-- how to create a table
CREATE TABLE our_teacher(
	teacher_id int,
    teacher_name varchar(120),
    age int,
    teacher_email varchar(120),
    teacher_contact varchar(10),
    dept varchar(50),
	address text,
    joining_date date
);

select * from our_teacher;

-------------------------------------------------------------------------------------

select * from morning_clg.our_teacher;

use morning_clg;

select * from our_teacher; -- crud

-- how to add up data in our table

insert into our_teacher values(
	102, "Kriss Sharma", 29, "krisssharma@gmail.com",
    "982348324", "ML", "this is Kriss sharma addrss",
    "2026-04-26"
    );





SQL
	--> DDL -- Data Defination Language
			----> table, database --- CRUD
            
    --> DML -- Data Manupulation Language
			----> Data realted queries --- CRUD
            
    --> DCL -- Data Control Language
			----> Permission related queries
            ----> grant, revoke
            
    --> TCL -- Transaction Control Langauge
			----> Commit, rollback





-----------------------------------------------------------------------------------------

select * from our_teacher;

-- we need to delete table
	-- ---> delete table data not schema
    -- ---> delete table data with schema
    
-- delete table data as well as schema    
drop table our_teacher;

-- this query delete only table data not schema(structure)
truncate table our_teacher;




------------------------------

-- Second highest salary
SELECT MAX(SALARY) FROM Employee WHERE SALARY < (SELECT MAX(SALARY) FROM Employee);

-- How to select distinct table data
select distinct * from Employee;
-- Find all records whose name starts with s
select * from emp where name like 's%'

-- How to delete duplicate records in sql
-- What is normalization in database?
-- Can we delete primary key of the table?
-- How to fetch limited number of records from the database like pagination?
-- How to create index in database?
-- How many types of indexes are in database?
--
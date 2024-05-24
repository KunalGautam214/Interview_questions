-- Second highest salary
SELECT MAX(SALARY) FROM Employee WHERE SALARY < (SELECT MAX(SALARY) FROM Employee);

-- How to select distinct table data
select distinct * from Employee;
-- Find all records whose name starts with s
select * from emp where name like 's%'

-- How to delete duplicate records in sql
DELETE t1 FROM your_table t1 INNER JOIN your_table t2 ON t1.id < t2.id WHERE t1.some_column = t2.some_column;

-- What is normalization in database?
-- Can we delete primary key of the table?
-- How to fetch limited number of records from the database like pagination?
SELECT * FROM products ORDER BY product_id LIMIT 10 OFFSET 0; -- Fetches the first 10 records
SELECT * FROM products ORDER BY product_id LIMIT 10 OFFSET 10; -- Fetches records 11-20

-- How to create index in database?
CREATE INDEX idx_active_employees ON employees (employee_id) WHERE is_active = true;

-- How many types of indexes are in database?
--
1. DELETE:
DELETE is a DML (Data Manipulation Language) command used to remove rows from a table based on specified conditions.
It's transactional, meaning it can be rolled back within a transaction to undo the changes made by the DELETE statement.
DELETE can selectively remove specific rows using a WHERE clause.
It removes rows one by one and generates individual transaction logs for each deleted row, which can impact performance for large operations.

2. TRUNCATE:
TRUNCATE is a DDL (Data Definition Language) command used to quickly remove all rows from a table.
It operates more efficiently than DELETE as it doesn't generate individual transaction logs for each deleted row.
TRUNCATE is not transactional and cannot be rolled back. It's faster than DELETE, especially for large tables,
because it deallocates data pages rather than removing rows one by one.

3. DROP:
DROP is a DDL (Data Definition Language) command used to delete an entire object (table, view, index, etc.) from the database.
It removes the entire structure and associated data permanently. It cannot be rolled back.
Once a table or object is dropped, it no longer exists in the database.

--

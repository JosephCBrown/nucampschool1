-- Part 4: Mutations

-- Management has decided it would like to designate employees as experts of 
-- zero or more categories, and they want the database to keep track of who is
-- an expert in what. 
-- Q: How will you satisfy this new requirement? 
-- A: To satisfy an ER diagram would need to be created.
-- Q: What type of relationship is this? (e.g. 1-1, 1-many, or many-to-many?) 
-- A: I beleive this is an example of 1-many relationship or Many to Many relationships. Key is each employee will have no categories or a lot of categories assigned to them. 
-- Feel free to fill in the blanks above with a comment or two.


-- 4.1: Create table
-- Write a SQL statement that creates a new table meeting the following criteria:
--   1. It is named employees_categories
--   2. It has a employee_id column of type INTEGER
--   3. It has a category_id column of type INTEGER
--   4. Its primary key is a tuple of (employee_id, category_id) pairs

CREATE TABLE employees_categories (
    employee_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY(employee_id,category_id)
);


-- 4.2: Alter table
-- Make the employee_id column of employees_categories reference the 
-- primary key column of employees.
ALTER TABLE employees_categories
ADD CONSTRAINT fk_employees_categories 
FOREIGN KEY (employee_id) 
REFERENCES employees;

-- 4.3: Alter table
-- Make the category_id column of employees_categories reference the 
-- primary key column of categories.
ALTER TABLE employees_categories
ADD CONSTRAINT fk_categories_employees
FOREIGN KEY (category_id) 
REFERENCES categories;

-- 4.4: Insert records
-- Write a query that inserts the following employee ID, category ID pairs 
-- into employees_categories:
-- (1,2), (3,4), (4,3), (4,4), (8,2), (1,8), (1,3), (1,6)
INSERT INTO employees_categories(employee_id,category_id)
VALUES (1,2), (3,4), (4,3), (4,4), (8,2), (1,8), (1,3), (1,6);


-- 4.5: Remove records
-- Write query that deletes all rows from employees_categories but does not 
-- delete the employees_categories table itself.
DELETE FROM employees_categories;

-- Bonus: Refer to the new management decision at the top of this file.  
-- Write a query that assigns all employees of the London office to be 
INSERT INTO employees_categories(city)
SELECT city FROM employees
INSERT INTO employees_categories(category_id)
VALUES ('Dairy Products')
WHERE city = 'London';


-- 4.6: Delete table
-- Write a query to delete the employees_categories table
DROP TABLE employees_categories;
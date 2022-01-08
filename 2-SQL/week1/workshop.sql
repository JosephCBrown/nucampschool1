-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'week1_workshop' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS week1_workshop;
CREATE DATABASE week1_workshop;
-- connect via psql
\c week1_workshop

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


---
--- CREATE tables
---

CREATE TABLE products (
    id SERIAL,
    name TEXT NOT NULL,
    discontinued BOOLEAN NOT NULL,
    supplier_id INT,
    category_id INT,
    PRIMARY KEY(id)
);


CREATE TABLE categories (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    picture TEXT,
    PRIMARY KEY (id)
);



-- TODO create more tables here...
CREATE TABLE suppliers (
    supplier_id SERIAL,
    supplier_name TEXT NOT NULL,
    PRIMARY KEY (supplier_id)
);
CREATE TABLE customers (
    customer_id SERIAL,
    company_name TEXT NOT NULL,
    PRIMARY KEY(customer_id)
    
);
CREATE TABLE employees (
    employee_id SERIAL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    PRIMARY KEY(employee_id)
    
);

CREATE TABLE orders (
    id SERIAL,
    date DATE,
    customer_id INT NOT NULL,
    employee_id INT,
    PRIMARY KEY(id)
);

CREATE TABLE orders_products (
    id INTEGER,
    product_id INTEGER, 
    discount NUMERIC,
    quantity NUMERIC
);  

CREATE TABLE territories (
    territory_id SERIAL PRIMARY KEY,
    description TEXT

);  
CREATE TABLE offices (
    territory_id SERIAL, 
    address_line TEXT

);  



CREATE TABLE employees_territories (
    employee_id INTEGER,
    territory_id INTEGER, 
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL

);

CREATE TABLE offices_territories (
    office_id INTEGER,
    territory_id INTEGER, 
    address_line TEXT NOT NULL

);

CREATE TABLE us_states (
    us_states_id TEXT,
    us_states_name TEXT, 
    us_states_abb TEXT 

);


---
--- Add foreign key constraints
---

ALTER TABLE products
ADD CONSTRAINT fk_products_categories 
FOREIGN KEY (category_id) 
REFERENCES categories;

-- TODO create more constraints here...

ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id) 
REFERENCES customers;

ALTER TABLE orders
ADD CONSTRAINT fk_orders_employee
FOREIGN KEY (employee_id) 
REFERENCES employees;

ALTER TABLE products
ADD CONSTRAINT fk_products_suppliers
FOREIGN KEY (supplier_id) 
REFERENCES suppliers;

ALTER TABLE orders_products
ADD CONSTRAINT fk_orders_products
FOREIGN KEY (id) 
REFERENCES products,
ADD CONSTRAINT fk_products_orders
FOREIGN KEY (id)
REFERENCES orders;

ALTER TABLE employees_territories
ADD CONSTRAINT fk_employees_territories
FOREIGN KEY (employee_id) 
REFERENCES employees,
ADD CONSTRAINT fk_territories_employees
FOREIGN KEY (territory_id)
REFERENCES territories;

ALTER TABLE offices
ADD CONSTRAINT fk_offices_territories
FOREIGN KEY (territory_id) 
REFERENCES territories;


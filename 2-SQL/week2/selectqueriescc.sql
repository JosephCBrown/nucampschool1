SELECT company_name
FROM customers
WHERE company_name >= 'Q' 
ORDER BY company_name DESC;

SELECT first_name, last_name
FROM employees
where title = 'Sales Representative'
ORDER BY last_name, first_name;

SELECT first_name, home_phone
FROM employees
where first_name like 'A%' AND home_phone like '%4%'
ORDER BY employee_id;
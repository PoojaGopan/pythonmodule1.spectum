CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(255) NOT NULL,
    emp_salary DECIMAL(10, 2),
    emp_department VARCHAR(50)
);
ALTER TABLE employee
ADD emp_address VARCHAR(255);
INSERT INTO employee (emp_id, emp_name, emp_salary, emp_department, emp_address)
VALUES
    (1, 'John Doe', 50000.00, 'IT', '123 Main Street'),
    (2, 'Jane Smith', 60000.50, 'HR', '456 Oak Avenue'),
    (3, 'Bob Johnson', 75000.75, 'Finance', '789 Pine Road');



Select * from employee;
UPDATE employee
SET emp_salary = 55000.00
WHERE emp_id = 1;
select * from employee;

SELECT *
FROM employee
WHERE emp_salary > 60000;

SELECT emp_id, emp_name
FROM employee;
DELETE FROM employee
WHERE emp_id = 1;
select * from employee;
ALTER TABLE employee
RENAME TO new_employee;
select * from new_employee;

ALTER TABLE new_employee
CHANGE COLUMN emp_department department_name VARCHAR (50);

select * from new_employee;
-- Select employees with a salary greater than 50000 and in the IT department
SELECT *
FROM new_employee
WHERE emp_salary > 50000
  AND department_name = 'HR';

SELECT *
FROM new_employee
WHERE (emp_salary > 70000 AND department_name  = 'HR')
   OR department_name  = 'Finance';
   
-- Select employees in the IT or HR department
SELECT *
FROM new_employee
WHERE department_name IN ('Finance', 'HR');


-- Select employees with a salary between 50000 and 70000
SELECT *
FROM new_employee
WHERE emp_salary BETWEEN 50000 AND 70000;


SELECT *
FROM employee
WHERE emp_name LIKE 'J%';--  the persons name starting with j 

SELECT department_name, COUNT(*) as total_employees
FROM new_employee
GROUP BY department_name;

SELECT department_name, AVG(emp_salary) as avg_salary
FROM new_employee
GROUP BY department_name;

SELECT MAX(emp_salary) AS min_salary
FROM new_employee;


SELECT department_name, AVG(emp_salary) AS average_salary
FROM new_employee
GROUP BY department_name
HAVING AVG(emp_salary) > 70000;
-- Find departments with a minimum salary greater than 50000 can also use max
SELECT department_name, MIN(emp_salary) AS min_salary
FROM new_employee
GROUP BY department_name
HAVING MIN(emp_salary) > 60000;




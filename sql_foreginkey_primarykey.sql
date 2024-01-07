-- Create the newclass table
CREATE TABLE newc(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    email VARCHAR(255)
);

-- Insert data into the newclass table
INSERT INTO newc(username, email)
VALUES ('pooja', '123@gmail.com'), ('ligy', '456@gmail.com');

-- Select data from the newclass table
SELECT * FROM newc;

-- Create the neworders table with a foreign key reference to newclass
CREATE TABLE newo (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES newc(user_id)
);

-- Insert data into the neworders table
INSERT INTO newo (user_id, order_date, total_amount)
VALUES (1, '2024-01-05', 150.00), (2, '2024-01-06', 120.00);

-- Select data from the neworders table
SELECT * FROM newo;

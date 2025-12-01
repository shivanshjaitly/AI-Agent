DROP DATABASE IF EXISTS finance;
CREATE DATABASE finance;
USE finance;

CREATE TABLE merchants (
    merchant_id INT PRIMARY KEY AUTO_INCREMENT,
    merchant_name VARCHAR(100),
    industry VARCHAR(50),
    country VARCHAR(50),
    created_at DATE
);

CREATE TABLE transactions (
    txn_id INT PRIMARY KEY AUTO_INCREMENT,
    merchant_id INT,
    txn_date DATE,
    order_value DECIMAL(12,2),
    revenue DECIMAL(12,2),
    status VARCHAR(20), -- SUCCESS, FAILED
    payment_mode VARCHAR(20),
    FOREIGN KEY (merchant_id) REFERENCES merchants(merchant_id)
);

CREATE TABLE bank_costs (
    cost_id INT PRIMARY KEY AUTO_INCREMENT,
    txn_id INT,
    cost_date DATE,
    cost_amount DECIMAL(10,2),
    FOREIGN KEY (txn_id) REFERENCES transactions(txn_id)
);

CREATE TABLE settlements (
    settlement_id INT PRIMARY KEY AUTO_INCREMENT,
    merchant_id INT,
    settlement_date DATE,
    settled_amount DECIMAL(12,2),
    FOREIGN KEY (merchant_id) REFERENCES merchants(merchant_id)
);

INSERT INTO merchants (merchant_name, industry, country, created_at) VALUES
('Amazon India', 'Ecommerce', 'India', '2022-01-10'),
('Flipkart', 'Ecommerce', 'India', '2022-05-20'),
('Swiggy', 'FoodTech', 'India', '2023-03-01'),
('Zomato', 'FoodTech', 'India', '2023-06-15');

INSERT INTO transactions (merchant_id, txn_date, order_value, revenue, status, payment_mode) VALUES

-- OCTOBER 2024
(1,'2024-10-05',8000, 400,'SUCCESS','UPI'),
(2,'2024-10-10',5000, 250,'SUCCESS','CARD'),
(4,'2024-10-15',7000, 350,'SUCCESS','UPI'),

-- NOVEMBER 2024
(1,'2024-11-02',9000, 450,'SUCCESS','CARD'),
(1,'2024-11-18',14000,700,'SUCCESS','UPI'),
(1,'2024-11-25',8000, 380,'SUCCESS','CARD'),

(2,'2024-11-11',12000,600,'SUCCESS','UPI'),
(2,'2024-11-22',7000,  350,'FAILED','CARD'),

(3,'2024-11-05',3000, 150,'SUCCESS','UPI'),
(3,'2024-11-20',4000, 200,'SUCCESS','CARD'),

(4,'2024-11-17',11000,550,'SUCCESS','UPI'),

-- DECEMBER 2024
(1,'2024-12-04',5000,250,'SUCCESS','UPI'),
(2,'2024-12-15',9000,450,'SUCCESS','CARD'),

-- 2024 Earlier (for YTD Margin)
(1,'2024-03-12',6000,300,'SUCCESS','UPI'),
(2,'2024-05-22',4000,200,'SUCCESS','CARD'),
(3,'2024-08-19',5000,250,'SUCCESS','UPI');

INSERT INTO bank_costs (txn_id, cost_date, cost_amount) VALUES
(1,'2024-10-05',45),
(2,'2024-10-10',25),
(3,'2024-10-15',30),

(4,'2024-11-02',60),
(5,'2024-11-18',80),
(6,'2024-11-25',50),
(7,'2024-11-11',55),
(9,'2024-11-05',20),
(10,'2024-11-20',30),
(11,'2024-11-17',65),

(12,'2024-12-04',35),
(13,'2024-12-15',40);

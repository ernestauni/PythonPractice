CREATE DATABASE web_store;

CREATE TABLE order_status(
    status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(255) NOT NULL);
   
CREATE TABLE customer(
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL);

CREATE TABLE category(
	category_id SERIAL PRIMARY KEY,
	cat_name VARCHAR(50) NOT NULL);

CREATE TABLE supplier(
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL);

CREATE TABLE products(
    products_id SERIAL PRIMARY KEY,
    prod_name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price FLOAT NOT NULL,
    warranty_period INTEGER NOT NULL,
    category_id BIGINT REFERENCES category(category_id),
    supplier_id BIGINT REFERENCES supplier(supplier_id));

CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY,
    customer_id BIGINT REFERENCES customer(customer_id),
    product_id BIGINT REFERENCES products(products_id),
    status_id BIGINT REFERENCES order_status(status_id),
	quantity INT NOT NULL);
   
   
    
INSERT INTO category (cat_name)
VALUES ('Portable computer'),
		('Monitor'),
		('Keyboard');
		
INSERT INTO supplier(supplier_name,phone,email)
VALUES ('TechLab','37069876543','techlab@email.com'),
		('PC parts','37064561239','pcparts@email.com'),
		('JohnWick','37066669998','jw@email.com');
		
INSERT INTO products (prod_name,description,price,warranty_period,category_id,supplier_id)
VALUES ('TV Monitor','Portable monitor, TV',359.99,12,2,1),
		('ASUS Zenbook','Portable computer, light, 2021',1300,12,1,1),
		('LT keyboard','Black LT keyboard',50.99,3,3,3);
		
INSERT INTO customer (first_name, last_name,phone, email)
VALUES ('John','Poul','37061478523','jp@emnail.com'),
		('Moana','Sea','37063698521','ms@emnail.com'),
		('Karen','Rich','37065289632','kr@emnail.com');

INSERT INTO order_status (status_name)
VALUES ('entered'),
		('in processing'),
		('(caceled'),
		('delivered'),
		('paid(done');

INSERT INTO orders (customer_id,product_id,status_id,quantity)
VALUES (1,1,1,2),
		(2,2,2,1),
		(3,3,3,1);
	
UPDATE customer 
SET phone='37061597532'
WHERE first_name='Moana' AND last_name='Sea';

DELETE FROM public.supplier WHERE supplier_id=2;

SELECT *
FROM customer 
WHERE first_name='John';

SELECT *
FROM products 
WHERE price>300
ORDER BY price DESC;

SELECT *
FROM orders 
WHERE status_id=2;

SELECT first_name,last_name
FROM customer c
JOIN orders o 
ON c.customer_id=o.customer_id
WHERE status_id=2;

SELECT prod_name, supplier_name, cat_name
FROM products p
JOIN supplier s 
ON p.supplier_id=s.supplier_id
JOIN category c
ON p.category_id=c.category_id
WHERE price>300;

SELECT *
FROM orders o
JOIN customer c 
ON c.customer_id=o.customer_id
JOIN products p
ON o.product_id=p.products_id
ORDER BY c.first_name;
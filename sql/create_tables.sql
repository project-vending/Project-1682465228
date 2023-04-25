SQL
-- Create the sales table
CREATE TABLE sales (
  sale_id int,
  customer_id int,
  order_id int,
  sale_amount decimal(10,2),
  sale_date date
);

-- Create the customers table
CREATE TABLE customers (
  customer_id int,
  customer_name varchar(255),
  customer_email varchar(255)
);

-- Create the orders table
CREATE TABLE orders (
  order_id int,
  customer_id int,
  order_date date,
  order_total decimal(10,2)
);

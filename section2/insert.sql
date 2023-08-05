-- Insert statement for manufacturers table
INSERT INTO manufacturers (manufacturer_id, name)
VALUES ('MFG001', 'ABC Electronics');

-- Insert statement for products table
INSERT INTO products (product_id, manufacturer_id, name, cost, weight)
VALUES ('P001', 'MFG001', 'Smartphone', 500.00, 0.3);

-- Insert statement for members table
INSERT INTO members (membership_id, name, email, address, mobile, password)
VALUES ('M001', 'John Doe', 'john.doe@example.com', '123 Main St', '123-456-7890', 'mypassword');

-- Insert statement for transactions table
INSERT INTO transactions (transaction_id, membership_id, date, payment_method)
VALUES ('T001', 'M001', '2023-08-05 10:30:00', 'Credit Card');

-- Insert statement for order_item table
INSERT INTO order_item (order_item_id, transaction_id, product_id, quantity)
VALUES ('OI001', 'T001', 'P001', 2);

-- Insert statement for delivery table
INSERT INTO delivery (delivery_id, order_item_id, deliverystatus)
VALUES ('D001', 'OI001', 'Shipped');

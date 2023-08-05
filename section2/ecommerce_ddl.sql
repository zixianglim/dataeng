CREATE TABLE IF NOT EXISTS products (
    product_id varchar(4000) PRIMARY KEY,
    manufacturer_id varchar(4000) NOT NULL,
    name varchar(4000) NOT NULL,
    cost numeric(100, 2) NOT NULL,
    weight numeric(10, 2) NOT NULL
);

CREATE TABLE IF NOT EXISTS manufacturers (
    manufacturer_id varchar(4000) PRIMARY KEY,
    name varchar(4000) NOT NULL
);

ALTER TABLE products DROP CONSTRAINT IF EXISTS fk_manufacturer;
ALTER TABLE products ADD CONSTRAINT fk_manufacturer
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id);

CREATE TABLE IF NOT EXISTS members (
    membership_id varchar(4000) PRIMARY KEY,
    name varchar(4000) NOT NULL,
    email varchar(4000) NOT NULL,
    address varchar(4000) NOT NULL,
    mobile varchar(4000) NOT NULL,
    password varchar(4000) NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id varchar(4000) PRIMARY KEY,
    membership_id varchar(4000) NOT NULL,
    date timestamp NOT NULL,
    payment_method varchar(4000) NOT NULL
);

ALTER TABLE transactions DROP CONSTRAINT IF EXISTS fk_membership;
ALTER TABLE transactions ADD CONSTRAINT fk_membership
    FOREIGN KEY (membership_id) REFERENCES members(membership_id);

CREATE TABLE IF NOT EXISTS order_item (
    order_item_id varchar(4000) PRIMARY KEY,
    transaction_id varchar(4000) NOT NULL,
    product_id varchar(4000) NOT NULL,
    quantity integer NOT NULL
);

ALTER TABLE order_item DROP CONSTRAINT IF EXISTS fk_transaction;
ALTER TABLE order_item ADD CONSTRAINT fk_transaction
    FOREIGN KEY (transaction_id) REFERENCES transactions(transaction_id);

ALTER TABLE order_item DROP CONSTRAINT IF EXISTS fk_product;
ALTER TABLE order_item ADD CONSTRAINT fk_product
    FOREIGN KEY (product_id) REFERENCES products(product_id);

CREATE TABLE IF NOT EXISTS delivery (
    delivery_id varchar(4000) PRIMARY KEY,
    order_item_id varchar(4000) NOT NULL,
    deliverystatus varchar(4000) NOT NULL
);

ALTER TABLE delivery DROP CONSTRAINT IF EXISTS fk_delivery;
ALTER TABLE delivery ADD CONSTRAINT fk_delivery
    FOREIGN KEY (order_item_id) REFERENCES order_item(order_item_id);

-- Get the total cost of item(s) purchased by a member in a transaction
SELECT
    t.transaction_id,
    t.membership_id,
    SUM(p.cost * oi.quantity) AS total_cost
FROM
    transactions t
JOIN
    order_item oi ON t.transaction_id = oi.transaction_id
JOIN
    products p ON oi.product_id = p.product_id
GROUP BY
    t.transaction_id,
    t.membership_id;


-- A manufacturer rebranding resulted in a change of the manufacturer's name only
UPDATE
    manufacturers
SET
    name = 'New Manufacturer Name'
WHERE
    manufacturer_id = 'MFG001';

SELECT * FROM manufacturers WHERE manufacturer_id = 'MFG001'

CREATE TABLE `customer` (
  `id` integer PRIMARY KEY AUTOINCREMENT,
  `f_name` string,
  `l_name` string,
  `email` string
)

CREATE TABLE `status` (
  `id` integer PRIMARY KEY,
  `name` string
)

CREATE TABLE `product` (
  `id` integer PRIMARY KEY AUTOINCREMENT,
  `name` string,
  `price` float
)

CREATE TABLE `order_` (
  `id` integer PRIMARY KEY AUTOINCREMENT,
  `customer_id` integer,
  `date_` string,
  `status_id` integer,
   FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
   FOREIGN KEY (`status_id`) REFERENCES `status` (`id`)
)

CREATE TABLE `product_order` (
  `order_id` integer,
  `product_id` integer,
  `quantity` integer,
   FOREIGN KEY (`order_id`) REFERENCES `order_` (`id`),
   FOREIGN KEY (`product_id`) REFERENCES `product` (`id`)
)

DROP TABLE product_order;

INSERT INTO customer (f_name, l_name, email)
VALUES 
('Renaldas', 'Zvegiukas', 'johndoe@splius.lt'),
('Jonas', 'Donce', 'janedoe@example.com'),
('Bobas', 'Marlejus', 'bobsmith@example.com'),
('Alice', 'Smith', 'alicesmith@example.com'),
('Chris', 'Lee', 'chrislee@example.com');

INSERT INTO order_ (customer_id, date_, status_id)
VALUES
(1, '2023-05-10', 1),
(2, '2023-05-09', 2),
(3, '2023-05-08', 1),
(4, '2023-05-07', 2),
(5, '2023-05-06', 1);

INSERT INTO product (name, price)
VALUES
('Sviestas', 2.99),
('Suris', 1.99),
('Kepenine', 2.99),
('Saslykai', 4.99),
('Pienas', 1.49);

INSERT INTO product_order (order_id, product_id, quantity)
VALUES
(1, 1, 2),
(1, 2, 1),
(2, 3, 2),
(2, 4, 3),
(3, 1, 3),
(3, 3, 1),
(4, 2, 2),
(4, 4, 1),
(5, 1, 1),
(5, 5, 2);

INSERT INTO status (id, name)
VALUES
(1, 'Patvirtintas'),
(2, 'apmokėtas'),
(3, 'įvykdytas'),
(4, 'atmestas');

-- kad rezultate matytųsi užsakymo id, pozicijos su kiekiais,
-- kainomis ir bendra pozicijos suma:
SELECT o.id AS "Order ID", 
       po.product_id AS "Product ID", 
       p.name AS "Product Name", 
       po.quantity AS "Quantity", 
       p.price AS "Price", 
       po.quantity * p.price AS "Total Price"
FROM order_ o 
JOIN product_order po ON o.id = po.order_id 
JOIN product p ON po.product_id = p.id;

-- padarykite, kad rezultate matytųsi užsakymo id,
-- užsakovo pavardė, data, bendra užsakymo suma
SELECT o.id AS order_id, c.l_name AS customer_last_name, o.date_ AS order_date, SUM(p.price * po.quantity) AS total_amount
FROM order_ o
JOIN customer c ON o.customer_id = c.id
JOIN product_order po ON o.id = po.order_id
JOIN product p ON po.product_id = p.id
GROUP BY o.id;

-- pirmos užklausos pagrindu sukurkite užklausą,
-- kurioje matytųsi, kiek ir kokio produkto buvo užsakyta
SELECT p.name AS product_name, c.f_name, SUM(po.quantity) AS total_quantity
FROM
product_order po
JOIN product p ON po.product_id = p.id
GROUP BY
po.product_id;
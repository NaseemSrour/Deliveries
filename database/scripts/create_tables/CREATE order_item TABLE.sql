CREATE TABLE order_item(
item_id int NOT NULL,
order_id int NOT NULL,
item_note varchar(50),
PRIMARY KEY(item_id, order_id),
FOREIGN KEY(item_id) REFERENCES item(item_id),
FOREIGN KEY(order_id) REFERENCES Orders(order_id)
);
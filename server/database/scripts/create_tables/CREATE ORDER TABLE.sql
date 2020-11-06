CREATE TABLE Orders(
order_id int NOT NULL AUTO_INCREMENT,
user_id int NOT NULL,
business_id int NOT NULL,
totalPrice int,
payment_method enum('cash', 'credit card'),
orderDate DATETIME,
orderEstTime TIME,
order_status enum('pending', 'rejected', 'approved', 'ready', 'fulfilled'),
PRIMARY KEY(order_id),
FOREIGN KEY(user_id) REFERENCES Users(user_id),
FOREIGN KEY(business_id) REFERENCES Business(business_id)
);
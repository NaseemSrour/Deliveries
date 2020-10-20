CREATE TABLE Item(
item_id int NOT NULL AUTO_INCREMENT,
item_name varchar(25) NOT NULL,
item_desc varchar(150),
image mediumblob,
price int NOT NULL,
business_id int NOT NULL,
PRIMARY KEY(item_id),
FOREIGN KEY(business_id) REFERENCES Business(business_id)
);
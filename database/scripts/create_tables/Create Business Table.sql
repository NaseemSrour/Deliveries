CREATE TABLE Business(
business_id int NOT NULL AUTO_INCREMENT,
business_name varchar(40) NOT NULL,
logo mediumblob,
tel varchar(10),
isOpen bit,
PRIMARY KEY(business_id)
);
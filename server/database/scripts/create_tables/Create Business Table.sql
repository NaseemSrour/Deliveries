CREATE TABLE Business(
business_id int NOT NULL AUTO_INCREMENT,
business_name varchar(40) NOT NULL,
business_owner_id int NOT NULL,
logo mediumblob,
tel varchar(10),
isOpen bit,
PRIMARY KEY(business_id),
FOREIGN KEY(business_owner_id) REFERENCES Users(user_id) 
);
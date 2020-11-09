CREATE TABLE Users(
user_id int NOT NULL AUTO_INCREMENT,
phone_number varchar(10) NOT NULL,
user_name varchar(25),
role ENUM('customer', 'owner', 'admin'),
PRIMARY KEY(user_id)
);

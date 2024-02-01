-- use testdatabase

-- CREATE TABLE orders (
--     order_id INT PRIMARY KEY AUTO_INCREMENT,
--     user_id INT,
--     product_name VARCHAR(255),
--     quantity INT,
--     FOREIGN KEY (user_id) REFERENCES users(user_id)
-- );

-- select * from users;
-- select * from orders;

-- select * from users
-- left join orders on users.user_id = orders.user_id

-- USE testdatabase;

-- create table users(
-- id int primary key auto_increment,
-- password varchar(4),
-- name varchar(3),
-- gender enum('male', 'female'),
-- email varchar(15),
-- birthday char(6),
-- age tinyint,
-- compay enum('samsung', 'lg', 'hyunday')
-- );

-- create table boards(
-- id int primary key auto_increment,
-- title varchar(5),
-- content varchar(10),
-- likes int check(likes between 1 and 100),
-- img char(1) default 'c',
-- created date,
-- user_id int,
-- foreign key(user_id) references users(id)
-- )


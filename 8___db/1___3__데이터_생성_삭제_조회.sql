-- create database testdatabase;
-- use testdatabase;

-- id int primary key, (primary key 고유한 값 생성.)
-- id 검색속도 햐상위해 primary key 설정
-- auto_increment id 1씩증가.
-- not null 빈값 안넣기
--  unique 유니크한 값
-- create table users(
-- 	id int auto_increment primary key,
--     username varchar(30) not null,
--     email varchar(100) unique,
--     is_business varchar(10) default false, -- 비즈니즈계정인지 체크
--     age int Check ( age >= 10 )users
-- )


-- use testdatabase;
-- create table users(
-- 	user_id int primary key,
--     name varchar(100),
--     age int
--     );

-- INSERT INTO users (user_id, name, age)
-- VALUES (1, 'Alice', 25),
--        (2, 'Bob', 30),
--        (3, 'Charlie', 22),
--        (4, 'David', 33),
--        (5, 'Eve', 28);

-- create table orders (
-- order_id int primary key,
-- user_id int,
-- order_date date
-- );

insert into orders (order_id, user_id, order_date)
values (101, 1, '2023-01-01'),
       (102, 2, '2023-02-01'),
       (103, 1, '2023-02-15'),
       (104, 3, '2023-03-01'),
       (105, 4, '2023-03-10');

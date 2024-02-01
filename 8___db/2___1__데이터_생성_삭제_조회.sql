-- use testdatabase;

-- CREATE TABLE users(
-- 	user_id INT PRIMARY KEY AUTO_INCREMENT,
-- 	username TEXT NOT NULL,
-- 	email TEXT NOT NULL,
-- 	age INTusers
-- );

-- INSERT INTO users(username, email, age) VALUES('inseop', 'inseop@naver.com', 25)
-- SELECT * FROM users

-- INSERT INTO users(username, email) VALUES('inseop2', 'inseop2@naver.com')

-- INSERT INTO users (username, email, age) VALUES
--     ('alice', 'alice@example.com', 30),
--     ('bob', 'bob@example.com', 28),
--     ('charlie', 'charlie@example.com', 35);



-- INSERT IGNORE INTO users (username, email, age) VALUES ('john_doe', 'john@example.com', 25);

-- SELECT * FROM users;

-- INSERT INTO users (username, email, age) VALUES ('john_doe', 'john@example.com', 25) ON DUPLICATE KEY UPDATE age = 100;


-- INSERT INTO users SET username='john', email='john@example.com', age=25;


-- SELECT DISTINCT age FROM users

-- SELECT age, age * 100 FROM users

-- SELECT age, age * 100 as AGE100 FROM users

-- SELECT * FROM users ORDER BY age asc, user_id asc

-- SELECT * FROM users LIMIT 2, 4;

-- SELECT age, COUNT(*) as AGE_COUNT FROM users GROUP BY age;

-- 나이에 따라 내림차순으로 순위 부여하여 조회
-- SELECT
--   username,
--   age,
--   ROW_NUMBER() OVER (ORDER BY age DESC) AS 'rank'
-- FROM users;

-- SET SQL_SAFE_UPDATES = 0;



-- UPDATE users
-- SET username = 'FAFCss'
-- WHERE age >= 28;
-- SELECT ROW_COUNT(); 


-- SELECT * FROM users

-- UPDATE users
-- set username = case
-- when age >= 30 then 'sesesesesese'
-- else 'young'
-- end;

-- update users
-- set username = 'zzaaaaaaa5'
-- where age > 25
-- limit 3;


-- delete from users where username = 'zzaaaaaaa5' limit 1;




-- select * from users;
use testdatabase;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(4),
    name VARCHAR(3),
    gender ENUM('male', 'female'),
    email VARCHAR(15),
    birthday CHAR(6),
    age TINYINT,
    company ENUM('samsung', 'lg', 'hyundai')
);

create table board (
	id int auto_increment primary key,
    title varchar(5),
    content varchar(10),
    likes int check (likes between 1 and 100),
    img char(1) default 'c',
    created date default current_timestamp,
    user_id int,
    foreign key (user_id) references user(id)
);
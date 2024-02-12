create database booksminiproject;
use booksminiproject;

CREATE TABLE books (
    isbn VARCHAR(13) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    publisher VARCHAR(255),
    publishing DATE,
    coverurl LONGTEXT
);

CREATE TABLE kyobo_ranking (
    rankingId INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputdate DATE,
    kyoborank INT,
    kyoborating DECIMAL(3,1),
    kyoboreview INT,
    kyoboupdown INT,
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);

CREATE TABLE kyobo_price (
    priceid INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputdate DATE,
    kyoboprice DECIMAL(10,2),
    kyobosaleprice DECIMAL(10,2),
    kyobopoint INT,
    kyobourl longtext,
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);


CREATE TABLE yes24_ranking (
    rankingid INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputdate DATE,
    yes24rank INT,
    yes24rating DECIMAL(3,1),
    yes24review INT,    
    yes24updown INT,
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);

CREATE TABLE yes24_price (
    priceid INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputdate DATE,
    yes24price DECIMAL(10,2),
    yes24saleprice DECIMAL(10,2),
    yes24point INT,
    yes24url longtext,
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);



CREATE TABLE average (
    priceid INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputdate DATE,
    averagerating DECIMAL(3,1),
    averageranking DECIMAL(3,1),
    averageweekranking DECIMAL(3,1),
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);
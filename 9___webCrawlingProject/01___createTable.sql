-- create database BooksMiniproject;
use BooksMiniproject;

CREATE TABLE Books (
    isbn VARCHAR(13) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    publisher VARCHAR(255),
    publishing DATE,
    coverUrl LONGTEXT
);

CREATE TABLE kyoboRanking (
    rankingId INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputDate DATE,
    kyoboRank INT,
    kyoboRating DECIMAL(3,1),
    kyoboReview INT,
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);

CREATE TABLE kyoboPrice (
    priceId INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputDate DATE,
    kyoboPrice DECIMAL(10,2),
    kyoboSalePrice DECIMAL(10,2),
    kyoboPoint INT,
    kyobourl longtext,
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);


CREATE TABLE yes24Ranking (
    rankingId INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputDate DATE,
    yes24Rank INT,
    yes24Rating DECIMAL(3,1),
    yes24Review INT,    
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);

CREATE TABLE yes24Price (
    priceId INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputDate DATE,
    yes24Price DECIMAL(10,2),
    yes24SalePrice DECIMAL(10,2),
    yes24Point INT,
    yes24url longtext,
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);



CREATE TABLE Average (
    priceId INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputDate DATE,
    averageRating DECIMAL(3,1),
    averageRanking DECIMAL(3,1),
    averageWeekRanking DECIMAL(3,1),
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);
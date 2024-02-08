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

CREATE TABLE Ranking (
    rankingId INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputDate DATE,
    kyoboRank INT,
    kyoboRating DECIMAL(3,1),
    kyoboReview INT,
    yes24Rank INT,
    yes24Rating DECIMAL(3,1),
    yes24Review INT,    
    FOREIGN KEY (isbn) REFERENCES books(isbn) ON DELETE CASCADE
);

CREATE TABLE Price (
    priceId INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(13),
    inputDate DATE,
    kyoboPrice DECIMAL(10,2),
    kyoboSalePrice DECIMAL(10,2),
    kyoboPoint INT,
    yes24Price DECIMAL(10,2),
    yes24SalePrice DECIMAL(10,2),
    yes24Point INT,
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
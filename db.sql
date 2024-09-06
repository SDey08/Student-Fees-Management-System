CREATE database stfeeman;

USE stfeeman;

CREATE TABLE Students (
    Sl INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    DOB VARCHAR(10) NOT NULL,
    Ph VARCHAR(15) NOT NULL,
    Email_id VARCHAR(100) NOT NULL UNIQUE,
    Adm_no VARCHAR(20) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE Payments (
    Sl INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Adm_no VARCHAR(20) NOT NULL,
    Amt DECIMAL(10, 2) NOT NULL,
    Pay_stat ENUM('Paid', 'Unpaid') NOT NULL,
    Month VARCHAR(20) NOT NULL
);

CREATE DATABASE HotelSurvey;
USE HotelSurvey;
CREATE TABLE Hotels (
    HotelID INT AUTO_INCREMENT,
    HotelName VARCHAR(255) NOT NULL,
    Location VARCHAR(255),
    PRIMARY KEY (HotelID)
);

CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Email VARCHAR(255),
    PRIMARY KEY (CustomerID)
);

CREATE TABLE Responses (
    ResponseID INT AUTO_INCREMENT,
    HotelID INT,
    CustomerID INT,
    StayDuration INT,
    BookingMethod VARCHAR(255),
    RoomSatisfaction INT,
    ServiceSatisfaction INT,
    Comments TEXT,
    PRIMARY KEY (ResponseID),
    FOREIGN KEY (HotelID) REFERENCES Hotels(HotelID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

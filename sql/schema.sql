DROP DATABASE IF EXISTS autism_app;
CREATE SCHEMA autism_app;
USE autism_app;

CREATE TABLE `User` (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64),
    age INT,
    gender VARCHAR(10),
    email VARCHAR(120) UNIQUE
);

CREATE TABLE DNA_Sequence (
    dna_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    sequence TEXT NOT NULL,
    responses JSON,
    evaluation VARCHAR(50),
    time_submitted TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES `User`(user_id)
        ON UPDATE CASCADE ON DELETE CASCADE
);
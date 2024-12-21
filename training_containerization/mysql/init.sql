-- Create a new database if it doesn't exist
CREATE DATABASE IF NOT EXISTS demo_mysql;

-- Use the newly created database
USE demo_mysql;

-- Create a 'users' table
CREATE TABLE IF NOT EXISTS users_feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    feedback VARCHAR(100) NOT NULL
);

-- Insert some initial data into the 'users' table
INSERT INTO users_feedback (name, feedback) VALUES ('Alice', 'Training is awesome');

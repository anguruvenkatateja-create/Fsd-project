CREATE DATABASE IF NOT EXISTS hostel_complaint_db;
USE hostel_complaint_db;

CREATE TABLE IF NOT EXISTS complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    issue TEXT NOT NULL,
    status ENUM('Pending', 'In Progress', 'Resolved') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE complaints ADD COLUMN status VARCHAR(20) DEFAULT 'Pending';
ALTER TABLE complaints ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
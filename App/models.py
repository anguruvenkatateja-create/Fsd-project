import mysql.connector
import os
from flask import current_app

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

class Complaint:
    @staticmethod
    def create(student_name, room_number, issue):
        db = get_db_connection()
        cursor = db.cursor()
        query = "INSERT INTO complaints (student_name, room_number, issue) VALUES (%s, %s, %s)"
        cursor.execute(query, (student_name, room_number, issue))
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def get_all():
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM complaints ORDER BY created_at DESC")
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results
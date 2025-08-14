#!/usr/bin/python3
"""
Creates the database alx_book_store in MySQL.
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (update user and password if needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',       # Change to your MySQL username
        password='Adisa@2718'    # Change to your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close cursor and connection
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
    except NameError:
        pass

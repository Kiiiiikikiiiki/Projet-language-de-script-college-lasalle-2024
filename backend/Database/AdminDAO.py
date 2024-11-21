import sqlite3
from backend.Class_Domain.Admin import Admin

class AdminDAO:
    def add_admin(conn: sqlite3.Connection, username: str, password_hash: str) -> bool:
        """
        Adds a new admin to the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            username (str): The username of the admin
            password_hash (str): The password hash of the admin
        Returns:
            bool: True if the admin was added successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO admin (username, password_hash) VALUES (?, ?)", (username, password_hash))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def update_admin(conn: sqlite3.Connection, admin: Admin) -> bool:
        """
        Updates an admin in the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            admin (Admin): The admin to modify
        Returns:
            bool: True if the admin was modified successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE admin SET username = ?, password_hash = ? WHERE admin_id = ?", (admin.username, admin.password_hash, admin.getAdmin_id()))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def delete_admin(conn: sqlite3.Connection, admin_id: int) -> bool:
        """
        Deletes an admin from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            admin_id (int): The id of the admin to delete
        Returns:
            bool: True if the admin was deleted successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM admin WHERE admin_id = ?", (admin_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False


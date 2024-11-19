import sqlite3

def obtenir_connection(db_name: str) -> sqlite3.Connection:
    """
    Attempts to open a connection to a sqlite database
    and returns it if successful.

    Args:
        db_name (str): The name of the path to the database to connect to
    Returns:
        sqlite3.Connection: The connection to the database, or None if an error occurs
    """
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None
    
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
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)
        return False
    
def add_member(conn: sqlite3.Connection, username: str, password_hash: str) -> bool:
    """
    Adds a new member to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        username (str): The username of the member
        password_hash (str): The password hash of the member
    Returns:
        bool: True if the member was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO member (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)
        return False
    
# TODO : Ajouter les autres functions utilitaires
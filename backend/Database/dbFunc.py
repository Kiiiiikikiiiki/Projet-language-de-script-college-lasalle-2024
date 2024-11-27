import sqlite3
import datetime

def obtenir_connection() -> sqlite3.Connection:
    """
    Attempts to open a connection to a sqlite database
    and returns it if successful.

    Args:
        db_name (str): The name of the path to the database to connect to
    Returns:
        sqlite3.Connection: The connection to the database, or None if an error occurs
    """
    try:
        conn = sqlite3.connect("backend/Database/munchyroll.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None
    
def fermer_connection(conn: sqlite3.Connection) -> None:
    """
    Closes the connection to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
    """
    conn.close()     
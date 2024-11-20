import sqlite3
import datetime
import backend.Class_Domain.Season as Season


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
        conn = sqlite3.connect(db_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
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
    
def add_anime(conn: sqlite3.Connection, anime_name: str, desc: str, rating: float,
              types: list[str], release_date: datetime.date = datetime.date.today()) -> bool:
    """
    Adds a new anime to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        anime_name (str): The name of the anime
        desc (str): The description of the anime    
        rating (float): The rating of the anime
        types (list[str]): The types of the anime
        release_date (datetime.date): The release date of the anime (defaults to today's date)
    Returns:
        bool: True if the anime was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO anime (anime_name, desc, rating, release_date) VALUES" +
                       "(?, ?, ?, ?)", (anime_name, desc, rating, release_date))
        
        anime_name = cursor.lastrowid
        
        for type in types:
            cursor.execute("INSERT INTO animeType (anime_name, type) VALUES (?, ?)",
                           (anime_name, type))
            
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)
        return False
    
def add_season(conn: sqlite3.Connection, season_name: str, anime_name: str,
               release_date: datetime.date = datetime.date.today()) -> bool:
    """
    Adds a new season to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        season_name (str): The name of the season
        anime_name (str): The name of the anime to which the season belongs
        release_date (datetime.date): The release date of the season (defaults to today's date)
    Returns:
        bool: True if the season was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO season (season_name, anime_name, release_date) VALUES" +
                       "(?, ?, ?)", (season_name, anime_name, release_date))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)
        return False

# TODO: Continue de rest of the functions
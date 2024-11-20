import sqlite3
import datetime

# region Function CRUD des tables principales

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
              types: list[str], picture_url: str, release_date: datetime.date = datetime.date.today()) -> bool:
    """
    Adds a new anime to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        anime_name (str): The name of the anime
        desc (str): The description of the anime    
        rating (float): The rating of the anime
        types (list[str]): The types of the anime
        picture_url (str): The url of the picture of the anime
        release_date (datetime.date): The release date of the anime (defaults to today's date)
    Returns:
        bool: True if the anime was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO anime (anime_name, desc, rating, picture_url, release_date) VALUES" +
                       "(?, ?, ?, ?, ?)", (anime_name, desc, rating, picture_url ,release_date))
        
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

def add_episode(conn : sqlite3.Connection, episode_name : str, rating : float, nb_like : int,
                nb_dislike : int, picture_url : str, season_id : int, release_date : datetime.date = datetime.date.today()) -> bool:
    """
    Adds a new episode to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        episode_name (str): The name of the episode
        rating (float): The rating of the episode
        nb_like (int): The number of likes for the episode
        nb_dislike (int): The number of dislikes for the episode
        picture_url (str): The url of the picture of the episode
        season_id (int): The id of the season to which the episode belongs
        release_date (datetime.date): The release date of the episode (defaults to today's date)
    Returns:
        bool: True if the episode was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO episode (episode_name, rating, nb_like, nb_dislike, picture_url, season_id, release_date) VALUES" +
                       "(?, ?, ?, ?, ?, ?, ?)", (episode_name, rating, nb_like, nb_dislike, picture_url, season_id, release_date))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:    
        print(e)
        return False
    
def add_comment(conn : sqlite3.Connection, comment_content : str, member_id : int,
                episode_id : int, nb_like : int, nb_dislike : int,
                creation_date : datetime.date = datetime.date.today()) -> bool:
    """
    Adds a new comment to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        comment_content (str): The content of the comment
        member_id (int): The id of the member who wrote the comment
        episode_id (int): The id of the episode to which the comment belongs
        nb_like (int): The number of likes for the comment
        nb_dislike (int): The number of dislikes for the comment
        creation_date (datetime.date): The creation date of the comment (defaults to today's date)
    Returns:
        bool: True if the comment was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO comment (comment_content, member_id, episode_id, nb_like, nb_dislike, creation_date) VALUES" +
                       "(?, ?, ?, ?, ?, ?)", (comment_content, member_id, episode_id, nb_like, nb_dislike, creation_date))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)
        return False

# endregion  

# region Function CRUD des tables d'association
def add_memberAnime(conn: sqlite3.Connection, member_id: int, anime_name: str) -> bool:
    """
    Adds a new member_anime to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        member_id (int): The id of the member
        anime_name (str): The name of the anime
    Returns:
        bool: True if the member_anime was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO memberAnime (member_id, anime_name) VALUES (?, ?)", (member_id, anime_name))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)
        return False
    
def add_animeType(conn: sqlite3.Connection, anime_name: str, type: str) -> bool:
    """
    Adds a new anime_type to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        anime_name (str): The name of the anime
        type (str): The type of the anime
    Returns:
        bool: True if the anime_type was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO animeType (anime_name, type) VALUES (?, ?)", (anime_name, type))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)
        return False

def add_commentComment(conn: sqlite3.Connection, parent_comment_id: int, child_comment_id: int) -> bool:
    """
    Adds a new comment_comment to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        parent_comment_id (int): The id of the parent comment    
        child_comment_id (int): The id of the child comment
    Returns:
        bool: True if the comment_comment was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO commentComment (comment_id, reply_id) VALUES (?, ?)", (parent_comment_id, child_comment_id))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)        
        return False

def add_ratingAnime(conn: sqlite3.Connection, member_id: int, anime_name: str, rating: float) -> bool:
    """
    Adds a new rating_anime to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        member_id (int): The id of the member
        anime_name (str): The name of the anime
        rating (float): The rating of the anime
    Returns:
        bool: True if the rating_anime was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ratingAnime (member_id, anime_name, rating) VALUES (?, ?, ?)", (member_id, anime_name, rating))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)
        return False

def add_ratingEpisode(conn: sqlite3.Connection, member_id: int, episode_id: int, rating: float) -> bool:
    """
    Adds a new rating_episode to the database

    Args:
        conn (sqlite3.Connection): The connection to the database
        member_id (int): The id of the member
        episode_id (int): The id of the episode
        rating (float): The rating of the episode
    Returns:
        bool: True if the rating_episode was added successfully, False otherwise
    """
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ratingEpisode (member_id, episode_id, rating) VALUES (?, ?, ?)", (member_id, episode_id, rating))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:        
        print(e)
        return False

# endregion
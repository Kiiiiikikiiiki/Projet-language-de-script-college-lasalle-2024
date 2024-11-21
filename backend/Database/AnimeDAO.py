import sqlite3
import datetime
from backend.Class_Domain.Anime import Anime

class AnimeDAO:
    
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
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def update_anime(conn: sqlite3.Connection, anime: Anime) -> bool:
        """
        Updates an existing anime in the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            anime (Anime): The anime to update
        Returns:
            bool: True if the anime was updated successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE anime SET anime_name = ?, desc = ?, rating = ?, picture_url = ?, release_date = ? , modification_date = ?" +
                        "WHERE anime_name = ?", (anime.anime_name, anime.desc, anime.rating, anime.picture_url, anime.release_date, datetime.date.today(), anime.anime_name))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def delete_anime(conn: sqlite3.Connection, anime_name: str) -> bool:
        """
        Deletes an existing anime from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            anime_name (str): The name of the anime to delete
        Returns:
            bool: True if the anime was deleted successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM anime WHERE anime_name = ?", (anime_name,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
import sqlite3
import datetime
from backend.Class_Domain.Season import Season

class SeasonDAO:
    
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
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def update_season(conn: sqlite3.Connection, season: Season) -> bool:
        """
        Updates a season in the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            season (Season): The season to update
        Returns:
            bool: True if the season was updated successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE season SET season_name = ?, anime_name = ?, release_date = ?, modification_date = ?" +
                        "WHERE season_id = ?", (season.season_name, season.anime_name, season.release_date, datetime.date.today(), season.getSeason_id()))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def delete_season(conn: sqlite3.Connection, season_id: int) -> bool:
        """
        Deletes a season from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            season_id (int): The id of the season to delete
        Returns:    
            bool: True if the season was deleted successfully, False otherwise
        """
        try:
            cursor = conn.cursor()            
            cursor.execute("DELETE FROM season WHERE season_id = ?", (season_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
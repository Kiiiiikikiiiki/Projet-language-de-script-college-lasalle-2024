import sqlite3
import datetime
from backend.Class_Domain.Episode import Episode

class EpisodeDAO:
    
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
            return True
        except sqlite3.Error as e:    
            print(e)
            return False
        
    def update_episode(conn: sqlite3.Connection, episode: Episode) -> bool:
        """
        Updates an existing episode in the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            episode (Episode): The episode to update
        Returns:
            bool: True if the episode was updated successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE episode SET episode_name = ?, rating = ?, nb_like = ?, nb_dislike = ?, picture_url = ?, release_date = ?, modification_date = ?" +
                        "WHERE episode_id = ?", (episode.episode_name, episode.rating, episode.nb_like, episode.nb_dislike, episode.picture_url, episode.release_date, datetime.date.today(), episode.getEpisode_id()))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            
    def delete_episode(conn: sqlite3.Connection, episode_id: int) -> bool:
        """
        Deletes an episode from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            episode_id (int): The id of the episode to delete
        Returns:    
            bool: True if the episode was deleted successfully, False otherwise
        """
        try:
            cursor = conn.cursor()            
            cursor.execute("DELETE FROM episode WHERE episode_id = ?", (episode_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:        
            print(e)
            return False
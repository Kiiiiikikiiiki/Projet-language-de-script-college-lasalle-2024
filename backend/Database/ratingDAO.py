import sqlite3

class RatingDAO:
    
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
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def update_ratingAnime(conn: sqlite3.Connection, member_id: int, anime_name: str, rating: float) -> bool:
        """
        Updates a rating_anime in the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            member_id (int): The id of the member
            anime_name (str): The name of the anime
            rating (float): The new rating of the anime
        Returns:
            bool: True if the rating_anime was updated successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE ratingAnime SET rating = ? WHERE member_id = ? AND anime_name = ?", (rating, member_id, anime_name))
            conn.commit()
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
            return True
        except sqlite3.Error as e:        
            print(e)
            return False
        
    def update_ratingEpisode(conn: sqlite3.Connection, member_id: int, episode_id: int, rating: float) -> bool:
        """
        Updates a rating_episode in the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            member_id (int): The id of the member
            episode_id (int): The id of the episode
            rating (float): The new rating of the episode
        Returns:
            bool: True if the rating_episode was updated successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE ratingEpisode SET rating = ? WHERE member_id = ? AND episode_id = ?", (rating, member_id, episode_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
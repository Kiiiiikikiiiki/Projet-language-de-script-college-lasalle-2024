import sqlite3
import datetime
from backend.Class_Domain.Comment import Comment

class CommentDAO:
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
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def update_comment(conn: sqlite3.Connection, comment: Comment) -> bool:
        """
        Updates a comment in the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            comment (Comment): The comment to modify
        Returns:
            bool: True if the comment was modified successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE comment SET comment_content = ?, nb_like = ?, nb_dislike = ? WHERE comment_id = ?", (comment.comment_content, comment.nb_like, comment.nb_dislike, comment.getComment_id()))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def delete_comment(conn: sqlite3.Connection, comment_id: int) -> bool:
        """
        Deletes a comment from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            comment_id (int): The id of the comment to delete
        Returns:
            bool: True if the comment was deleted successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM comment WHERE comment_id = ?", (comment_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False    
        
    def get_comment_by_id(conn: sqlite3.Connection, comment_id: int) -> Comment:
        """
        Gets a comment from the database by its id

        Args:
            conn (sqlite3.Connection): The connection to the database
            comment_id (int): The id of the comment
        Returns:
            Comment: The comment with the given id
        """
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comment WHERE comment_id = ?", (comment_id,))
            row = cursor.fetchone()
            if row is not None:
                return Comment(row[1], CommentDAO.get_replys_by_comment_id(conn, row[0]), row[4], row[5], row[6], row[0], row[2], row[3])
            else:
                return None
        except sqlite3.Error as e:
            print(e)
            return None
        
    def get_replys_by_comment_id(conn: sqlite3.Connection, comment_id: int) -> list:
        """
        Gets the replys of a comment from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            comment_id (int): The id of the comment
        Returns:
            list: The list of replys
        """
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT reply_id FROM commentComment WHERE comment_id = ?", (comment_id,))
            rows = cursor.fetchall()
            if len(rows) > 0:
                replys = []
                for row in rows:
                    cursor.execute("SELECT * FROM comment WHERE comment_id = ?", (row[0],))
                    rowComment = cursor.fetchone()
                    replys.append(Comment(rowComment[1], CommentDAO.get_replys_by_comment_id(conn, rowComment[0]), rowComment[4], rowComment[5], rowComment[6], rowComment[0], rowComment[2], rowComment[3]))
                return replys
            else:
                return []
        except sqlite3.Error as e:
            print(e)
            return []
        
    def get_comments_by_episode_id(conn: sqlite3.Connection, episode_id: int) -> list:
        """
        Gets the comments of an episode from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            episode_id (int): The id of the episode
        Returns:
            list: The list of comments
        """
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comment WHERE episode_id = ?", (episode_id,))
            rows = cursor.fetchall()
            if len(rows) > 0:
                comments = []
                for row in rows:
                    comments.append(CommentDAO.get_comment_by_id(conn, row[0]))
                return comments
            else:
                return []
        except sqlite3.Error as e:
            print(e)
            return []
        
    def get_comments_by_member_id(conn: sqlite3.Connection, member_id: int) -> list:
        """
        Gets the comments of a member from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            member_id (int): The id of the member
        Returns:
            list: The list of comments
        """
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comment WHERE member_id = ?", (member_id,))
            rows = cursor.fetchall()
            if len(rows) > 0:
                comments = []
                for row in rows:
                    comments.append(CommentDAO.get_comment_by_id(conn, row[0]))
                return comments
            else:
                return []
        except sqlite3.Error as e:
            print(e)
            return []
    
    
import sqlite3
from backend.Class_Domain.Member import Member
from backend.Database.CommentDAO import CommentDAO
from backend.Class_Domain.User import User

class MemberDAO:
    
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
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def update_member(conn: sqlite3.Connection, member: Member) -> bool:
        """
        Updates a member in the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            member (Member): The member to modify
        Returns:
            bool: True if the member was modified successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE member SET username = ?, password_hash = ? WHERE member_id = ?", (member.username, member.password_hash, member.id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def delete_member(conn: sqlite3.Connection, member_id: int) -> bool:
        """
        Deletes a member from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            member_id (int): The id of the member to delete
        Returns:
            bool: True if the member was deleted successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM member WHERE member_id = ?", (member_id,))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
        
    def get_member(conn: sqlite3.Connection, member_id: int) -> Member:
        """
        Gets a member from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            member_id (int): The id of the member to get
        Returns:
            Member: The member with the specified id
        """
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM member WHERE member_id = ?", (member_id,))
            memberRow = cursor.fetchone()
            if memberRow is not None:
                animeList = MemberDAO.get_anime_list(conn, member_id)
                return Member(memberRow[1], memberRow[2], animeList, memberRow[3], MemberDAO.get_comment_list(conn, member_id), int(memberRow[0]))
            else:
                return None
        except sqlite3.Error as e:
            print(e)
            
    def getAll_Members(conn: sqlite3.Connection) -> list:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM member")
            memberList = cursor.fetchall()
            return [MemberDAO.get_member(conn, row[0]) for row in memberList]
        except sqlite3.Error as e:
            print(e)
            
    def get_anime_list(conn: sqlite3.Connection, member_id: int) -> list:
        """
        Gets the anime list of a member from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            member_id (int): The id of the member
        Returns:
            list: The anime list of the member        
        """
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT anime_name FROM memberAnime WHERE member_id = ?", (member_id,))
            animeList = cursor.fetchall()
            return [row[0] for row in animeList]
        except sqlite3.Error as e:
            print(e)
            return []

    def get_comment_list(conn: sqlite3.Connection, member_id: int) -> list:
        """
        Gets the comment list of a member from the database

        Args:
            conn (sqlite3.Connection): The connection to the database
            member_id (int): The id of the member
        Returns:
            list: The comment list of the member        
        """
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT comment_id FROM comment WHERE member_id = ?", (member_id,))
            commentList = cursor.fetchall()
            return [CommentDAO.get_comment_by_id(conn, row[0]) for row in commentList]
        except sqlite3.Error as e:
            print(e)
            return []
        
    def add_anime_to_member(conn: sqlite3.Connection, member_id: int, anime_name: str) -> bool:
        """
        Adds an anime to a member's anime list

        Args:
            conn (sqlite3.Connection): The connection to the database
            member_id (int): The id of the member
            anime_name (str): The name of the anime
        Returns:
            bool: True if the anime was added successfully, False otherwise
        """
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO memberAnime (member_id, anime_name) VALUES (?, ?)", (member_id, anime_name))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def verifyMember(conn: sqlite3.Connection, username: str, password: str) -> bool:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM member WHERE username = ? AND password_hash = ?", 
                           (username, User.get_hash_password(password)))
            row = cursor.fetchone()
            return row is not None
        except sqlite3.Error as e:
            print(e)
            return False
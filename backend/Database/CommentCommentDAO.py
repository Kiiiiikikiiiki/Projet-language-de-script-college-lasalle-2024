import sqlite3

class CommentCommentDAO:
    def add_commentComment(conn: sqlite3.Connection, parent_comment_id: int, child_comment_id: int) -> bool:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO commentComment (comment_id, reply_id) VALUES (?, ?)", (parent_comment_id, child_comment_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
        
    def delete_commentComment(conn: sqlite3.Connection, parent_comment_id: int, child_comment_id: int) -> bool:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM commentComment WHERE comment_id = ? AND reply_id = ?", (parent_comment_id, child_comment_id))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
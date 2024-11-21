import backend.Database.dbFunc as dbFunc
from backend.Database.MemberDAO import MemberDAO
from backend.Class_Domain.Member import Member
from backend.Class_Domain.Comment import Comment
from backend.Database.CommentDAO import CommentDAO
from backend.Database.CommentCommentDAO import CommentCommentDAO
from backend.Class_Domain.User import User
from backend.Database.AdminDAO import AdminDAO
from backend.Database.MemberDAO import MemberDAO
from backend.Database.AnimeDAO import AnimeDAO





conn = dbFunc.obtenir_connection("backend/Database/munchyroll.db")


# #Création des admins
# AdminDAO.add_admin(conn, "Luffy", User.get_hash_password("1234"))
# AdminDAO.add_admin(conn, "Law", User.get_hash_password("5678"))
# AdminDAO.add_admin(conn, "Zoro", User.get_hash_password("12345"))



# #Création des membres
# MemberDAO.add_member(conn, "Alejo0105", User.get_hash_password("Berrio"))
# MemberDAO.add_member(conn, "Gino12", User.get_hash_password("Noel"))
# MemberDAO.add_member(conn, "Justin2004", User.get_hash_password("Coco"))
# MemberDAO.add_member(conn, "Diego1984", User.get_hash_password("Cosmo"))
# MemberDAO.add_member(conn, "User345", User.get_hash_password("User"))
#types=[]
#Création des animes
#AnimeDAO.add_anime(conn, "Demon Slayer: Kimetsu no Yaiba", 
#                 """We are in Japan's Taisho era. Tanjiro, a young boy who makes a living selling charcoal, discovers one day that his family has been murdered by a demon. To make matters worse, his younger sister Nezuko, the sole survivor of the massacre, has been transformed into a demon.
#                 Devastated by these events, Tanjiro decides to become a Demon Slayer to restore his sister to normal and avenge his family by killing the demon responsible for the massacre.""",
#                 5,types,"./Image/Animes/anime1/anime1.png")

# cursor = conn.cursor()
# cursor.execute("DELETE FROM anime WHERE anime_name = 'Demon Slayer: Kimetsu no Yaiba'")
# conn.commit()

#conn.close()
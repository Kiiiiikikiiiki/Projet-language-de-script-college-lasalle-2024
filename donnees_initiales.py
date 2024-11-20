import backend.Database.dbFunc as dbFunc
from backend.Class_Domain.User import User

conn = dbFunc.obtenir_connection("backend/Database/munchyroll.db")


#Création des admins
dbFunc.add_admin(conn, "Luffy", User.get_hash_password("1234"))
dbFunc.add_admin(conn, "Law", User.get_hash_password("5678"))

#Création des membres
dbFunc.add_member(conn, "Alejo0105", User.get_hash_password("Berrio"))
dbFunc.add_member(conn, "Gino12", User.get_hash_password("Noel"))
dbFunc.add_member(conn, "Justin2004", User.get_hash_password("Coco"))
dbFunc.add_member(conn, "Diego1984", User.get_hash_password("Cosmo"))
dbFunc.add_member(conn, "User345", User.get_hash_password("User"))



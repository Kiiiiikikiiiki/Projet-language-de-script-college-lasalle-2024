import backend.Database.dbFunc as dbFunc
from backend.Class_Domain.User import User
from backend.Database.AdminDAO import AdminDAO
from backend.Database.MemberDAO import MemberDAO
from backend.Database.AnimeDAO import AnimeDAO
from backend.Database.SeasonDAO import SeasonDAO
from backend.Database.EpisodeDAO import EpisodeDAO
from backend.Database.ratingDAO import RatingDAO
from backend.Database.CommentDAO import CommentDAO
from backend.Database.CommentCommentDAO import CommentCommentDAO


conn = dbFunc.obtenir_connection("backend/Database/munchyroll.db")


# #Création des admins
# AdminDAO.add_admin(conn, "Luffy", User.get_hash_password("1234"))
# AdminDAO.add_admin(conn, "Law", User.get_hash_password("5678"))




# #Création des membres
# MemberDAO.add_member(conn, "Alejo0105", User.get_hash_password("Berrio"))
# MemberDAO.add_member(conn, "Gino12", User.get_hash_password("Noel"))
# MemberDAO.add_member(conn, "Justin2004", User.get_hash_password("Coco"))
# MemberDAO.add_member(conn, "Diego1984", User.get_hash_password("Cosmo"))
# MemberDAO.add_member(conn, "User345", User.get_hash_password("User"))

#Création des animes
# AnimeDAO.add_anime(conn, "Demon Slayer: Kimetsu no Yaiba", 
#                 """We are in Japan's Taisho era. Tanjiro, a young boy who makes a living selling charcoal, discovers one day that his family has been murdered by a demon. To make matters worse, his younger sister Nezuko, the sole survivor of the massacre, has been transformed into a demon.
#                 Devastated by these events, Tanjiro decides to become a Demon Slayer to restore his sister to normal and avenge his family by killing the demon responsible for the massacre.""",
#                 5, ["Action", "Fantasy"],"./Image/Animes/anime1/anime1.png")

# AnimeDAO.add_anime(conn, "Attack on Titan",
#                    """Many years ago, humanity was on the brink of extinction with the emergence of giant creatures that devoured everyone in their path. Fleeing for their lives, humanity managed to survive in a fortified city with towering walls, which became the last bastion of civilization against the Titans roaming freely across the world. Now, that peace is about to be shattered by a series of events that will reveal what the Titans are and how they came to be.""",
#                    4.5, ["Action", "Adventure", "Drama", "Fantasy", "Thriller"], "./Image/Animes/anime2/anime2.png")

# AnimeDAO.add_anime(conn, "Dragon Ball Super",
#                    """Dragon Ball returns with a new series after many years! New enemies, powerful new transformations, and fresh characters will shape the future of the beloved heroes.
#                     Get excited, enjoy, and have fun with Son Goku, Vegeta, Gohan, and the rest of their companions!""",
#                     4, ["Action", "Fantasy", "Sci-Fi"], "./Image/Animes/anime3/anime3.png")

# AnimeDAO.add_anime(conn, "One Piece",
#                    """Embark on the adventure of a lifetime with One Piece. This epic anime series, created by the renowned mangaka Eiichiro Oda, is a global phenomenon that has captivated the hearts of fans across generations for over 25 years. This thrilling high-seas journey is filled with unbreakable friendship, epic battles for freedom, and the relentless pursuit of dreams. Join Monkey D. Luffy and his lovable pirate crew as they uncover the true meaning of power and justice.

#                    Monkey D. Luffy refuses to let anything or anyone stand in his way of becoming the King of the Pirates. Armed with supernatural powers from a Devil Fruit, this young and spirited pirate is on a quest to find the legendary treasure known as the One Piece. He sets a course for the treacherous waters of the Grand Line, recruiting a colorful crew to form the Straw Hat Pirates. As their captain, Luffy is determined to sail onward until he and his friends achieve their dreams!""",
#                    5, ["Action", "Adventure", "Fantasy"], "./Image/Animes/anime4/anime4.png")

# AnimeDAO.add_anime(conn, "DandaDan",
#                    """When Momo, a high school student from a family of spiritual mediums, meets her classmate Okarun, an occult enthusiast, they clash over their beliefs: Momo believes in ghosts but not aliens, while Okarun believes in aliens but not ghosts. When it turns out that both phenomena are real, Momo awakens a hidden power, and Okarun gains the strength of a curse. Together, they must face the paranormal forces threatening their world.""",
#                    4, ["Action", "Adventure", "Fantasy"], "./Image/Animes/anime5/anime5.png")

"""Création des seasons"""
"""
Anime 1. Demon Slayer: Kimetsu no Yaiba
Saison 1 (4 episodes)
Saison 2 (2 episodes)
Saison 3 (3 episodes)
"""
# SeasonDAO.add_season(conn, "Saison 1", "Demon Slayer: Kimetsu no Yaiba")
# EpisodeDAO.add_episode(conn,"Episode 1 S1", 3, 100, 20, "./Image/Animes/anime1/s1/ep1.png", 1)
# EpisodeDAO.add_episode(conn,"Episode 2 S1", 3, 150, 10, "./Image/Animes/anime1/s1/ep2.png", 1)
# EpisodeDAO.add_episode(conn,"Episode 3 S1", 3, 200, 10, "./Image/Animes/anime1/s1/ep3.png", 1)
# EpisodeDAO.add_episode(conn,"Episode 4 S1", 3, 250, 10, "./Image/Animes/anime1/s1/ep4.png", 1)

# SeasonDAO.add_season(conn, "Saison 2", "Demon Slayer: Kimetsu no Yaiba")
# EpisodeDAO.add_episode(conn,"Episode 1 S2", 3, 300, 10, "./Image/Animes/anime1/s2/ep1.png", 2)
# EpisodeDAO.add_episode(conn,"Episode 2 S2", 3, 350, 10, "./Image/Animes/anime1/s2/ep2.png", 2)

# SeasonDAO.add_season(conn, "Saison 3", "Demon Slayer: Kimetsu no Yaiba")
# EpisodeDAO.add_episode(conn,"Episode 1 S3", 3, 400, 10, "./Image/Animes/anime1/s3/ep1.png", 3)
# EpisodeDAO.add_episode(conn,"Episode 2 S3", 3, 450, 10, "./Image/Animes/anime1/s3/ep2.png", 3)
# EpisodeDAO.add_episode(conn,"Episode 3 S3", 3, 500, 10, "./Image/Animes/anime1/s3/ep3.png", 3)

"""
Anime 2. Attack on Titan
Saison 1 (3 episodes)
Saison 2 (2 episodes)
Saison 3 (2 episodes)
"""

# SeasonDAO.add_season(conn, "Saison 1", "Attack on Titan")
# EpisodeDAO.add_episode(conn,"Episode 1 S1", 3, 100, 20, "./Image/Animes/anime2/s1/ep1.png", 4)
# EpisodeDAO.add_episode(conn,"Episode 2 S1", 3, 150, 10, "./Image/Animes/anime2/s1/ep2.png", 4)
# EpisodeDAO.add_episode(conn,"Episode 3 S1", 3, 200, 10, "./Image/Animes/anime2/s1/ep3.png", 4)

# SeasonDAO.add_season(conn, "Saison 2", "Attack on Titan")
# EpisodeDAO.add_episode(conn,"Episode 1 S2", 3, 300, 10, "./Image/Animes/anime2/s2/ep1.png", 5)
# EpisodeDAO.add_episode(conn,"Episode 2 S2", 3, 350, 10, "./Image/Animes/anime2/s2/ep2.png", 5)

# SeasonDAO.add_season(conn, "Saison 3", "Attack on Titan")
# EpisodeDAO.add_episode(conn,"Episode 1 S3", 3, 400, 10, "./Image/Animes/anime2/s3/ep1.png", 6)
# EpisodeDAO.add_episode(conn,"Episode 2 S3", 3, 450, 10, "./Image/Animes/anime2/s3/ep2.png", 6)

"""
Anime 3. Dragon Ball Super
Saison 1 (4 episodes)
"""
# SeasonDAO.add_season(conn, "Saison 1", "Dragon Ball Super")
# EpisodeDAO.add_episode(conn,"Episode 1 S1", 3, 100, 20, "./Image/Animes/anime3/s1/ep1.png", 7)
# EpisodeDAO.add_episode(conn,"Episode 2 S1", 3, 150, 10, "./Image/Animes/anime3/s1/ep2.png", 7)
# EpisodeDAO.add_episode(conn,"Episode 3 S1", 3, 200, 10, "./Image/Animes/anime3/s1/ep3.png", 7)
# EpisodeDAO.add_episode(conn,"Episode 4 S1", 3, 250, 10, "./Image/Animes/anime3/s1/ep4.png", 7)

"""
Anime 4. One Piece
Saison 1 (4 episodes)
Saison 2 (3 episodes)
Saison 3 (2 episodes)
"""
# SeasonDAO.add_season(conn, "Saison 1", "One Piece")
# EpisodeDAO.add_episode(conn,"Episode 1 S1", 3, 100, 20, "./Image/Animes/anime4/s1/ep1.png", 8)
# EpisodeDAO.add_episode(conn,"Episode 2 S1", 3, 150, 10, "./Image/Animes/anime4/s1/ep2.png", 8)
# EpisodeDAO.add_episode(conn,"Episode 3 S1", 3, 200, 10, "./Image/Animes/anime4/s1/ep3.png", 8)
# EpisodeDAO.add_episode(conn,"Episode 4 S1", 3, 250, 10, "./Image/Animes/anime4/s1/ep4.png", 8)

# SeasonDAO.add_season(conn, "Saison 2", "One Piece")
# EpisodeDAO.add_episode(conn,"Episode 1 S2", 3, 300, 10, "./Image/Animes/anime4/s2/ep1.png", 9)
# EpisodeDAO.add_episode(conn,"Episode 2 S2", 3, 350, 10, "./Image/Animes/anime4/s2/ep2.png", 9)
# EpisodeDAO.add_episode(conn,"Episode 3 S2", 3, 400, 10, "./Image/Animes/anime4/s2/ep3.png", 9)

# SeasonDAO.add_season(conn, "Saison 3", "One Piece")
# EpisodeDAO.add_episode(conn,"Episode 1 S3", 3, 450, 10, "./Image/Animes/anime4/s3/ep1.png", 10)
# EpisodeDAO.add_episode(conn,"Episode 2 S3", 3, 500, 10, "./Image/Animes/anime4/s3/ep2.png", 10)

"""
Anime 5. DandaDan
Saison 1 (2 episodes)
"""

# SeasonDAO.add_season(conn, "Saison 1", "DandaDan")
# EpisodeDAO.add_episode(conn,"Episode 1 S1", 3, 100, 20, "./Image/Animes/anime5/s1/ep1.png", 11)
# EpisodeDAO.add_episode(conn,"Episode 2 S1", 3, 150, 10, "./Image/Animes/anime5/s1/ep2.png", 11)

"""Ajouter animes dans la liste des membres"""
"""
Member 1. Alejo0105
Demon Slayer: Kimetsu no Yaiba
Attack on Titan
Dragon Ball Super
One Piece
DandaDan
"""
# MemberDAO.add_anime_to_member(conn, 1, "Demon Slayer: Kimetsu no Yaiba")
# MemberDAO.add_anime_to_member(conn, 1, "Attack on Titan")
# MemberDAO.add_anime_to_member(conn, 1, "Dragon Ball Super")
# MemberDAO.add_anime_to_member(conn, 1, "One Piece")
# MemberDAO.add_anime_to_member(conn, 1, "DandaDan")

"""
Member 2. Gino12
Attack on Titan
One Piece
DandaDan
"""
# MemberDAO.add_anime_to_member(conn, 2, "Attack on Titan")
# MemberDAO.add_anime_to_member(conn, 2, "One Piece")
# MemberDAO.add_anime_to_member(conn, 2, "DandaDan")

"""
Member 3. Justin2004
Dragon Ball Super
One Piece
"""
# MemberDAO.add_anime_to_member(conn, 3, "Dragon Ball Super")
# MemberDAO.add_anime_to_member(conn, 3, "One Piece")

"""
Member 4. Diego1984
Demon Slayer: Kimetsu no Yaiba
Attack on Titan
Dragon Ball Super
DandaDan
"""
# MemberDAO.add_anime_to_member(conn, 4, "Demon Slayer: Kimetsu no Yaiba")
# MemberDAO.add_anime_to_member(conn, 4, "Attack on Titan")
# MemberDAO.add_anime_to_member(conn, 4, "Dragon Ball Super")
# MemberDAO.add_anime_to_member(conn, 4, "DandaDan")

"""
Member 5. User345
One Piece
DandaDan
"""
# MemberDAO.add_anime_to_member(conn, 5, "One Piece")
# MemberDAO.add_anime_to_member(conn, 5, "DandaDan")


"""Ajouter raitings Anime"""

"""
Member 1. Alejo0105
Demon Slayer: Kimetsu no Yaiba - 4
Attack on Titan - 4.5
Dragon Ball Super - 3.5
One Piece - 5
DandaDan - 4.3
"""
# RatingDAO.add_ratingAnime(conn, 1, "Demon Slayer: Kimetsu no Yaiba", 4)
# RatingDAO.add_ratingAnime(conn, 1, "Attack on Titan", 4.5)
# RatingDAO.add_ratingAnime(conn, 1, "Dragon Ball Super", 3.5)
# RatingDAO.add_ratingAnime(conn, 1, "One Piece", 5)
# RatingDAO.add_ratingAnime(conn, 1, "DandaDan", 4.3)

"""
Member 2. Gino12
Attack on Titan - 5
One Piece - 5
DandaDan - 3.8
"""
# RatingDAO.add_ratingAnime(conn, 2, "Attack on Titan", 5)
# RatingDAO.add_ratingAnime(conn, 2, "One Piece", 5)
# RatingDAO.add_ratingAnime(conn, 2, "DandaDan", 3.8)

"""
Member 3. Justin2004
Dragon Ball Super - 5
One Piece - 4.7
"""
# RatingDAO.add_ratingAnime(conn, 3, "Dragon Ball Super", 5)
# RatingDAO.add_ratingAnime(conn, 3, "One Piece", 4.7)

"""
Member 4. Diego1984
Demon Slayer: Kimetsu no Yaiba - 3.3
Attack on Titan - 4.2
Dragon Ball Super - 3.2
DandaDan - 4.4
"""
# RatingDAO.add_ratingAnime(conn, 4, "Demon Slayer: Kimetsu no Yaiba", 3.3)
# RatingDAO.add_ratingAnime(conn, 4, "Attack on Titan", 4.2)
# RatingDAO.add_ratingAnime(conn, 4, "Dragon Ball Super", 3.2)
# RatingDAO.add_ratingAnime(conn, 4, "DandaDan", 4.4)

"""
Member 5. User345
One Piece - 4.8
DandaDan - 4.1
"""
# RatingDAO.add_ratingAnime(conn, 5, "One Piece", 4.8)
# RatingDAO.add_ratingAnime(conn, 5, "DandaDan", 4.1)


"""Ajouter raitings Episode"""
"""
Member 1. Alejo0105
Demonslayer: Kimetsu no Yaiba S2 E2 - 4.8
Attack on Titan S1 E1 - 5
Attack on Titan S3 E2 - 4.5
One Piece S3 E1 - 4.8
One Piece S3 E2 - 5
"""
# RatingDAO.add_ratingEpisode(conn, 1, 6, 4.8)
# RatingDAO.add_ratingEpisode(conn, 1, 10, 5)
# RatingDAO.add_ratingEpisode(conn, 1, 16, 4.5)
# RatingDAO.add_ratingEpisode(conn, 1, 28, 4.8)
# RatingDAO.add_ratingEpisode(conn, 1, 29, 5)

"""
Member 2. Gino12
Attack on Titan S1 E1 - 4
Attack on Titan S2 E2 - 4.7
One Piece S2 E1 - 4.8
One Piece S3 E2 - 5
"""
# RatingDAO.add_ratingEpisode(conn, 2, 10, 4)
# RatingDAO.add_ratingEpisode(conn, 2, 14, 4.7)
# RatingDAO.add_ratingEpisode(conn, 2, 25, 4.8)
# RatingDAO.add_ratingEpisode(conn, 2, 29, 5)


"""
Member 3. Justin2004
Dragon Ball Super S1 E1 - 5
One Piece S1 E1 - 4.8
One Piece S3 E1 - 5
"""
# RatingDAO.add_ratingEpisode(conn, 3, 17, 5)
# RatingDAO.add_ratingEpisode(conn, 3, 21, 4.8)
# RatingDAO.add_ratingEpisode(conn, 3, 28, 5)

"""
Member 4. Diego1984
Demon Slayer: Kimetsu no Yaiba S1 E1 - 3.3
Attack on Titan S1 E1 - 4.2
Dragon Ball Super S1 E1 - 3.2
DandaDan S1 E1 - 4.4
"""
# RatingDAO.add_ratingEpisode(conn, 4, 1, 3.3)
# RatingDAO.add_ratingEpisode(conn, 4, 10, 4.2)
# RatingDAO.add_ratingEpisode(conn, 4, 17, 3.2)
# RatingDAO.add_ratingEpisode(conn, 4, 30, 4.4)

"""
Member 5. User345
One Piece S2 E1 - 4.8
DandaDan S1 E1 - 4.1
"""
# RatingDAO.add_ratingEpisode(conn, 5, 25, 4.8)
# RatingDAO.add_ratingEpisode(conn, 5, 30, 4.1)


"""Ajouter commentaires"""

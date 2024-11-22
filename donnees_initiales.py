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
"""
Episodes avec des commentaires test
ID=1 Demon Slayer: Kimetsu no Yaiba S1 E1
ID=6 Demon Slayer: Kimetsu no Yaiba S2 E2
ID=13 Attack on Titan S2 E1
ID=16 Attack on Titan S3 E2
ID=20 Dragon Ball Super S1 E4
ID=23 One Piece S1 E3
ID=25 One Piece S2 E1
ID=28 One Piece S3 E1
ID=31 DandaDan S1 E2
"""

"""Episode ID=1 Demon Slayer: Kimetsu no Yaiba S1 E1"""
# CommentDAO.add_comment(conn, "Great start to the series!", 1, 1, 12, 0) #ID 1
# CommentDAO.add_comment(conn, "Animation quality is amazing.", 2, 1, 10, 1) #ID 2
# CommentDAO.add_comment(conn, "The story feels very engaging so far.", 3, 1, 9, 0)  #ID 3
# CommentDAO.add_comment(conn, "Tanjiro's character is very likable.", 4, 1, 8, 0)  #ID 4
# CommentDAO.add_comment(conn, "Loved the emotional opening.", 5, 1, 15, 2)  #ID 5

#Replies
# CommentDAO.add_comment(conn, "Absolutely agree, it's top-notch!", 3, 1, 4, 0)  
# CommentDAO.add_comment(conn, "Yeah, the animation really stands out.", 2, 1, 5, 0) 
# CommentDAO.add_comment(conn, "I teared up a bit too, not gonna lie.", 1, 1, 3, 1)  

# CommentCommentDAO.add_commentComment(conn, 1, 6)
# CommentCommentDAO.add_commentComment(conn, 2, 7)
# CommentCommentDAO.add_commentComment(conn, 5, 8)

"""Episode ID=6 Demon Slayer: Kimetsu no Yaiba S2 E2"""
# CommentDAO.add_comment(conn, "This season's pace is much better.", 1, 6, 13, 1)  # ID 9
# CommentDAO.add_comment(conn, "Loved the new villain introduction.", 2, 6, 11, 0)  # ID 10
# CommentDAO.add_comment(conn, "Tanjiro's development is so satisfying.", 3, 6, 10, 0)  # ID 11
# CommentDAO.add_comment(conn, "Nezuko stole the show in this one!", 4, 6, 9, 1)  # ID 12
# CommentDAO.add_comment(conn, "This is shaping up to be even better than S1.", 5, 6, 14, 0) # ID 13

# Replies
# CommentDAO.add_comment(conn, "The pacing makes it way more enjoyable.", 1, 6, 4, 0)  
# CommentDAO.add_comment(conn, "Nezuko's moments were epic, agreed.", 3, 6, 6, 1)  
# CommentDAO.add_comment(conn, "Villain introductions are always a highlight.", 2, 6, 5, 0)  

# CommentCommentDAO.add_commentComment(conn, 9, 14)
# CommentCommentDAO.add_commentComment(conn, 12, 15)
# CommentCommentDAO.add_commentComment(conn, 10, 16)


"""Episode ID=13 Attack on Titan S2 E1"""
# CommentDAO.add_comment(conn, "The suspense was killing me!", 1, 13, 12, 0)  # ID 17
# CommentDAO.add_comment(conn, "Eren is such a compelling protagonist.", 2, 13, 9, 0)  # ID 18
# CommentDAO.add_comment(conn, "The Titans are as terrifying as ever.", 3, 13, 11, 1)  # ID 19
# CommentDAO.add_comment(conn, "The OST gave me chills!", 4, 13, 15, 0)  # ID 20
# CommentDAO.add_comment(conn, "This episode's ending was wild.", 5, 13, 13, 0)  # ID 21

# Replies
# CommentDAO.add_comment(conn, "Totally, the music added so much tension.", 1, 13, 5, 0)  
# CommentDAO.add_comment(conn, "Eren's choices are always fascinating to watch.", 2, 13, 7, 1)  
# CommentDAO.add_comment(conn, "That cliffhanger was insane!", 3, 13, 6, 0)  

# CommentCommentDAO.add_commentComment(conn, 20, 22)
# CommentCommentDAO.add_commentComment(conn, 18, 23)
# CommentCommentDAO.add_commentComment(conn, 21, 24)


"""Episode ID=16 Attack on Titan S3 E2"""
# CommentDAO.add_comment(conn, "Best episode of the season so far.", 1, 16, 14, 0)  # ID 25
# CommentDAO.add_comment(conn, "Levi is a total beast!", 2, 16, 16, 0)  # ID 26
# CommentDAO.add_comment(conn, "The twists just keep getting better.", 3, 16, 12, 1)  # ID 27
# CommentDAO.add_comment(conn, "Every moment felt so intense.", 4, 16, 10, 0)  # ID 28
# CommentDAO.add_comment(conn, "Can't wait to see what happens next.", 5, 16, 17, 0)  # ID 29

# # Replies
# CommentDAO.add_comment(conn, "Levi never fails to impress.", 1, 16, 5, 0)  
# CommentDAO.add_comment(conn, "I was on the edge of my seat too!", 2, 16, 4, 0)  
# CommentDAO.add_comment(conn, "This episode was a rollercoaster.", 3, 16, 6, 1)  

# CommentCommentDAO.add_commentComment(conn, 26, 30)
# CommentCommentDAO.add_commentComment(conn, 28, 31)
# CommentCommentDAO.add_commentComment(conn, 27, 32)


"""Episode ID=20 Dragon Ball Super S1 E4"""
# CommentDAO.add_comment(conn, "Classic Dragon Ball fun.", 1, 20, 9, 0)  # ID 33
# CommentDAO.add_comment(conn, "Goku always manages to make me laugh.", 2, 20, 8, 0)  # ID 34
# CommentDAO.add_comment(conn, "The action scenes were incredible!", 3, 20, 12, 1)  # ID 35
# CommentDAO.add_comment(conn, "Great mix of humor and action.", 4, 20, 7, 0)  # ID 36
# CommentDAO.add_comment(conn, "Dragon Ball never disappoints.", 5, 20, 10, 0)  # ID 37

# # Replies
# CommentDAO.add_comment(conn, "Absolutely, the humor was spot-on.", 1, 20, 3, 0)  
# CommentDAO.add_comment(conn, "I loved the action too, classic Goku.", 2, 20, 5, 0)  
# CommentDAO.add_comment(conn, "DB nostalgia hits hard.", 3, 20, 4, 0)  

# CommentCommentDAO.add_commentComment(conn, 36, 38)
# CommentCommentDAO.add_commentComment(conn, 35, 39)
# CommentCommentDAO.add_commentComment(conn, 33, 40)


"""Episode ID=23 One Piece S1 E3"""
# CommentDAO.add_comment(conn, "The humor in this episode was spot-on.", 1, 23, 11, 0)  # ID 41
# CommentDAO.add_comment(conn, "Luffy's antics never get old.", 2, 23, 14, 0)           # ID 42
# CommentDAO.add_comment(conn, "The crew's dynamic is so entertaining!", 3, 23, 10, 0)  # ID 43
# CommentDAO.add_comment(conn, "Loved the pacing of this episode.", 4, 23, 8, 0)        # ID 44
# CommentDAO.add_comment(conn, "The ending scene was so emotional.", 5, 23, 15, 0)      # ID 45

# # Replies
# CommentDAO.add_comment(conn, "Totally agree, especially Luffy's moments!", 3, 23, 6, 0)  
# CommentDAO.add_comment(conn, "Their chemistry makes every episode better.", 4, 23, 5, 0)  
# CommentDAO.add_comment(conn, "The ending hit me hard too, very touching.", 2, 23, 7, 0)  

# CommentCommentDAO.add_commentComment(conn, 42, 46)
# CommentCommentDAO.add_commentComment(conn, 43, 47)
# CommentCommentDAO.add_commentComment(conn, 45, 48)


"""Episode ID=25 One Piece S2 E1"""
# CommentDAO.add_comment(conn, "Great start to this arc, can't wait for more!", 1, 25, 12, 0)  # ID 49
# CommentDAO.add_comment(conn, "Sanji's cooking scene was hilarious!", 2, 25, 9, 0)           # ID 50
# CommentDAO.add_comment(conn, "The fight choreography was amazing!", 3, 25, 13, 0)           # ID 51
# CommentDAO.add_comment(conn, "The foreshadowing is very well done.", 4, 25, 11, 0)          # ID 52
# CommentDAO.add_comment(conn, "This arc has so much potential.", 5, 25, 10, 0)               # ID 53

# # Replies
# CommentDAO.add_comment(conn, "Sanji always makes me laugh too!", 1, 25, 6, 0)  
# CommentDAO.add_comment(conn, "Absolutely, the fights are top-notch.", 3, 25, 8, 0)  
# CommentDAO.add_comment(conn, "I love how they hint at future events subtly.", 5, 25, 7, 0)  

# CommentCommentDAO.add_commentComment(conn, 50, 54)
# CommentCommentDAO.add_commentComment(conn, 51, 55)
# CommentCommentDAO.add_commentComment(conn, 52, 56)


"""Episode ID=28 One Piece S3 E1"""
# CommentDAO.add_comment(conn, "The Straw Hat crew is unstoppable!", 1, 28, 13, 0)    # ID 57
# CommentDAO.add_comment(conn, "The villain introduction was perfect.", 2, 28, 11, 0)  # ID 58
# CommentDAO.add_comment(conn, "Usopp's moments were hilarious!", 3, 28, 10, 0)       # ID 59
# CommentDAO.add_comment(conn, "Nami's character is growing a lot.", 4, 28, 12, 0)    # ID 60
# CommentDAO.add_comment(conn, "This episode was pure One Piece goodness.", 5, 28, 14, 0)  # ID 61

# # Replies
# CommentDAO.add_comment(conn, "Their teamwork is unbeatable.", 2, 28, 7, 0)  
# CommentDAO.add_comment(conn, "I agree, the villain feels very threatening.", 1, 28, 8, 0)  
# CommentDAO.add_comment(conn, "Nami has really come a long way as a character.", 4, 28, 6, 0)  

# CommentCommentDAO.add_commentComment(conn, 57, 62)
# CommentCommentDAO.add_commentComment(conn, 58, 63)
# CommentCommentDAO.add_commentComment(conn, 60, 64)


"""Episode ID=31 DandaDan S1 E2"""
# CommentDAO.add_comment(conn, "DanDaDan is a fresh and unique series!", 1, 31, 15, 0)  # ID 65
# CommentDAO.add_comment(conn, "The art style really stands out.", 2, 31, 13, 0)        # ID 66
# CommentDAO.add_comment(conn, "This episode had some great action scenes.", 3, 31, 12, 0)  # ID 67
# CommentDAO.add_comment(conn, "I love how weird and fun this show is.", 4, 31, 10, 0)  # ID 68
# CommentDAO.add_comment(conn, "The pacing is so well-balanced.", 5, 31, 11, 0)         # ID 69

# # Replies
# CommentDAO.add_comment(conn, "It's definitely one of the most unique shows out there.", 2, 31, 7, 0)  # Responde al comentario ID 65
# CommentDAO.add_comment(conn, "The action scenes were top-tier, I agree!", 3, 31, 9, 0)  # Responde al comentario ID 67
# CommentDAO.add_comment(conn, "The humor is weird but works perfectly.", 5, 31, 8, 0)  # Responde al comentario ID 68

# CommentCommentDAO.add_commentComment(conn, 65, 70)
# CommentCommentDAO.add_commentComment(conn, 67, 71)
# CommentCommentDAO.add_commentComment(conn, 68, 72)
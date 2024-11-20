import sqlite3
from dbFunc import obtenir_connection

# Connection a la base de données
conn = obtenir_connection("backend/Database/munchyroll.db")

# region Création des tables principales dans la bd
cursor = conn.cursor()

# Table admin
cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin (
        admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
''')

# Table member
cursor.execute('''
    CREATE TABLE IF NOT EXISTS member (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        profile_picture TEXT
    )
''')

# Table anime
cursor.execute('''
    CREATE TABLE IF NOT EXISTS anime (
        anime_name TEXT PRIMARY KEY,
        desc TEXT NOT NULL,
        rating REAL NOT NULL CHECK(rating >= 0 AND rating <= 5),
        picture_url TEXT,
        release_date DATE NOT NULL,
        modification_date DATE
    )        
''')

# Table Season
cursor.execute('''
    CREATE TABLE IF NOT EXISTS season (
        season_id INTEGER PRIMARY KEY AUTOINCREMENT,
        season_name TEXT NOT NULL,
        anime_name TEXT NOT NULL,
        release_date DATE NOT NULL,
        modification_date DATE,
        
        FOREIGN KEY (anime_name) REFERENCES anime(anime_name)
    )
''')

# Table episode
cursor.execute('''
    CREATE TABLE IF NOT EXISTS episode (
        episode_id INTEGER PRIMARY KEY AUTOINCREMENT,
        episode_name TEXT NOT NULL,
        rating REAL NOT NULL CHECK(rating >= 0 AND rating <= 5),
        nb_like INTEGER NOT NULL,
        nb_dislike INTEGER NOT NULL,
        picture_url TEXT,
        season_id INTEGER NOT NULL,
        release_date DATE NOT NULL,
        modification_date DATE,
        
        FOREIGN KEY (season_id) REFERENCES season(season_id)
    )
''')

# Table comment 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS comment (
        comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        comment_content TEXT NOT NULL,
        member_id INTEGER NOT NULL,
        episode_id INTEGER NOT NULL,
        nb_like INTEGER NOT NULL,
        nb_dislike INTEGER NOT NULL,
        creation_date DATE NOT NULL,
        
        FOREIGN KEY (member_id) REFERENCES member(member_id),
        FOREIGN KEY (episode_id) REFERENCES episode(episode_id)
    )
''')
# endregion

# region Création des tables d'association

# Table memberAnime
cursor.execute('''
    CREATE TABLE IF NOT EXISTS memberAnime (
        member_id INTEGER NOT NULL,
        anime_name TEXT NOT NULL,
        
        PRIMARY KEY (member_id, anime_name),
        FOREIGN KEY (member_id) REFERENCES member(member_id),
        FOREIGN KEY (anime_name) REFERENCES anime(anime_name)
    )
''')

# Table animeType
cursor.execute('''
    CREATE TABLE IF NOT EXISTS animeType (
        anime_name TEXT NOT NULL,
        type TEXT NOT NULL,
        
        PRIMARY KEY (anime_name, type),
        FOREIGN KEY (anime_name) REFERENCES anime(anime_name)
    )
''')

# Table commentComment
cursor.execute('''
    CREATE TABLE IF NOT EXISTS commentComment (
        comment_id INTEGER NOT NULL,
        reply_id INTEGER NOT NULL,
        
        PRIMARY KEY (comment_id, reply_id),
        FOREIGN KEY (comment_id) REFERENCES comment(comment_id),
        FOREIGN KEY (reply_id) REFERENCES comment(comment_id)
    )
''')

# Table ratingAnime
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ratingAnime (
        member_id INTEGER NOT NULL,
        anime_name TEXT NOT NULL,
        rating REAL NOT NULL CHECK(rating >= 0 AND rating <= 5),
        
        PRIMARY KEY (member_id, anime_name),
        FOREIGN KEY (member_id) REFERENCES member(member_id),
        FOREIGN KEY (anime_name) REFERENCES anime(anime_name)
    )
''')

# Table ratingEpisode
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ratingEpisode (
        member_id INTEGER NOT NULL,
        episode_id INTEGER NOT NULL,
        rating REAL NOT NULL CHECK(rating >= 0 AND rating <= 5),
        
        PRIMARY KEY (member_id, episode_id),
        FOREIGN KEY (member_id) REFERENCES member(member_id),
        FOREIGN KEY (episode_id) REFERENCES episode(episode_id)
    )
''')

# endregion

cursor.close()
conn.commit()
conn.close()
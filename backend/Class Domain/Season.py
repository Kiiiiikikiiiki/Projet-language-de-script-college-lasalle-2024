import datetime
import Episode

class Season:
    """
    Create a season that will be part of an anime
    """
    
    def __init__(self, season_name : str, episodes : list[Episode.Episode], release_date : datetime.date,
                 modification_date : datetime.date = None, season_id : int = None, anime_name : str = None):
        """
        Constructor for a Season object.

        :param season_id: Unique identifier for the season defaults to None if not building the class for database.
        :param season_name: Name of the season.
        :param episodes: List of episodes in the season.
        :param anime_name: Name of the anime to which the season belongs (defaults to None if not building the class for database).
        :param release_date: Release date of the season.
        :param modification_date: Modification date of the season, defaults to None.
        """
        self.__season_id = season_id
        self.season_name = season_name
        self.episodes = episodes
        self.__anime_name = anime_name
        self.release_date = release_date
        self.__modification_date = modification_date
        
    # getters and setters
    def getSeason_id(self):
        return self.__season_id
    
    def getAnime_name(self):
        return self.__anime_name
    
    def getModification_date(self):
        return self.__modification_date
    
    def setSeason_id(self, season_id):
        self.__season_id = season_id
        
    def setAnime_name(self, anime_name):
        self.__anime_name = anime_name
        
    def setModification_date(self, modification_date):
        self.__modification_date = modification_date
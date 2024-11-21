import datetime
import backend.Class_Domain.Season as Season

class Anime:
    """
    Create an anime that users can add to their watchlist
    """
    
    def __init__(self, anime_name : str, desc : str, seasons : list[Season.Season], rating : float, types: list[str],
                 picture_url: str,release_date: datetime.date, modification_date: datetime.date = None):
        """
        Constructor for an anime object
        :param anime_name: name of the anime
        :param desc: description of the anime
        :param seasons: list of seasons that the anime have.
        :param rating: rating of the anime (between 0 and 5 inclusive)
        :param types: list of types of the anime
        :param picture_url: url of the picture of the anime
        :param release_date: release date of the anime
        :param modification_date: modification date of the anime, defaults to None
        """
        self.anime_name = anime_name
        self.desc = desc
        self.seasons = seasons
        self.rating = rating
        self.types = types
        self.picture_url = picture_url
        self.release_date = release_date
        self.__modification_date = modification_date
        
        
    # getters and setters
    def getModification_date(self):
        return self.__modification_date
    
    def setModification_date(self, modification_date):
        self.__modification_date = modification_date
import datetime
import backend.Class_Domain.Comment as Comment

class Episode:
    """
    Create an episode that will be part of a season
    """
    
    def __init__(self, episode_name : str, comments : list[Comment.Comment], rating : float, nb_like : int,
                 nb_dislike : int, picture_url : str, release_date : datetime.date, modification_date : datetime.date = None,
                 episode_id : int = None, season_id : int = None):
        """
        Constructor for an Episode object.

        :param episode_id: Unique identifier for the episode (defaults to None if not building the class for database).
        :param episode_name: Name of the episode.
        :param comments: List of comments related to the episode.
        :param rating: Rating of the episode (between 0 and 5 inclusive).
        :param nb_like: Number of likes for the episode.
        :param nb_dislike: Number of dislikes for the episode.
        :param picture_url: URL of the picture associated with the episode.
        :param season_id: Unique identifier of the season to which the episode belongs (defaults to None if not building the class for database).
        :param release_date: Release date of the episode.
        :param modification_date: Modification date of the episode, defaults to None.
        """
        self.__episode_id = episode_id
        self.episode_name = episode_name
        self.comments = comments
        self.rating = rating
        self.nb_like = nb_like
        self.nb_dislike = nb_dislike
        self.picture_url = picture_url
        self.__season_id = season_id
        self.release_date = release_date
        self.__modification_date = modification_date
        
    # Getters and setters
    def getEpisode_id(self):
        return self.__episode_id
    
    def getSeason_id(self):
        return self.__season_id
    
    def getModification_date(self):
        return self.__modification_date
    
    def setEpisode_id(self, episode_id):
        self.__episode_id = episode_id
        
    def setSeason_id(self, season_id):
        self.__season_id = season_id
        
    def setModification_date(self, modification_date):
        self.__modification_date = modification_date
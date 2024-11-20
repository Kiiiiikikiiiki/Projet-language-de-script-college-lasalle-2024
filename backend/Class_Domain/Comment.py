import datetime

class Comment:
    """
    Create a comment that is written by a member and assigned to an episode of an anime
    """
    
    def __init__(self, comment_content : str, comments : list, nb_like : int, nb_dislike : int,
                 creation_date: datetime.date, comment_id : int = None, member_id : int = None, episode_id : int = None):
        """
        Constructor for a Comment object
        
        :param comment_id: Unique identifier for the comment (defaults to None if not building the class for database)
        :param comment_content: Content of the comment
        :param member_id: Unique identifier of the member who wrote the comment (defaults to None if not building the class for database)
        :param episode_id: Unique identifier of the episode to which the comment is assigned (defaults to None if not building the class for database)
        :param comments: List of comments that are replies to this comment
        :param nb_like: Number of likes for the comment
        :param nb_dislike: Number of dislikes for the comment
        :param creation_date: Creation date of the comment
        """
        self.__comment_id = comment_id
        self.comment_content = comment_content
        self.__member_id = member_id
        self.__episode_id = episode_id
        self.comments = comments
        self.nb_like = nb_like
        self.nb_dislike = nb_dislike
        self.creation_date = creation_date
        
    # Getters and setters
    def getComment_id(self):
        return self.__comment_id
    
    def getMember_id(self):
        return self.__member_id
    
    def getEpisode_id(self):
        return self.__episode_id
    
    def setComment_id(self, comment_id):
        self.__comment_id = comment_id
        
    def setMember_id(self, member_id):
        self.__member_id = member_id
        
    def setEpisode_id(self, episode_id):
        self.__episode_id = episode_id
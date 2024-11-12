import User
import Anime
import Comment

class Member(User.User):
    """
    Class Member is a subclass of User\n
    Create a member that will be able to navigate and interact on the web application
    """
    
    def __init__(self, username : str, password_hash : str, anime_list: list[Anime.Anime],
                 profile_picture : str, comments : list[Comment.Comment], member_id : int = None):
        """
        Constructor for a Member object
        :param username: username of the member
        :param password_hash: password hash of the member
        :param member_id: Unique identifier for the member, defaults to None if not building the class for database
        :param anime_list: list of anime the member has watched
        :param profile_picture: profile picture of the member
        :param comments: comments the member has written
        """
        super().__init__(username, password_hash)
        self.__member_id = member_id
        self.anime_list = anime_list
        self.profile_picture = profile_picture
        self.comments = comments
        
    # Getters and Setters 
    def getMember_id(self):
        return self.__member_id

    def setMember_id(self, member_id):
        self.__member_id = member_id
        
    # Méthodes de classe
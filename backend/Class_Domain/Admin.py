import backend.Class_Domain.User as User


class Admin(User.User):
    """
    Class Admin is a subclass of User\n
    Create an administrator that will have admin privileges in the web application
    """
    def __init__(self, username, password_hash, admin_id : int = None):
        """
        Constructor for an admin object
        :param username: username of the admin
        :param password_hash: password hash of the admin
        :param admin_id: id of the admin
        """
        super().__init__(username, password_hash)
        self.__admin_id = admin_id
        
    # Getters and setters 
    def getAdmin_id(self):
        return self.__admin_id    
    
    def setAdmin_id(self, admin_id):        
        self.__admin_id = admin_id
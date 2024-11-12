import hashlib

class User:
    """
    Abstract class for any type of user
    """
    def __init__(self, username, password_hash):
        """
        Constructor for a User object
        :param username: username of the user
        :param password_hash: password hash of the user
        """
        self.username = username
        self.password_hash = password_hash
        
    @classmethod
    def get_hash_password(cls, password):
        """
        Get the hash of the password for the first time

        Args:
            password (str): the password to hash

        Returns:
            str: the hashed password
        """
        return str(hashlib.sha256(password.encode()).hexdigest())
    
    @classmethod
    def check_password(cls, password, password_hash):
        """
        Check if the password is correct

        Args:
            password (str): the password to check
            password_hash (str): the hash to compare with

        Returns:
            bool: True if the password is correct
        """
        return cls.get_hash_password(password) == password_hash
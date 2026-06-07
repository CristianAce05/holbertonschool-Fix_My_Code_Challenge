#!/usr/bin/python3
"""User class with hashed password"""
import hashlib


class User:
    """User class"""

    def __init__(self):
        """Initialize User"""
        self.__password = None

    @property
    def password(self):
        """Getter for password"""
        return self.__password

    @password.setter
    def password(self, pwd):
        """Setter for password - stores MD5 hash"""
        if pwd is None or not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        """Validates the password by comparing MD5 hashes"""
        if pwd is None or not isinstance(pwd, str):
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest() == self.__password


if __name__ == '__main__':
    print("Test User")
    u = User()
    u.password = "myPassword"
    if u.is_valid_password("myPassword"):
        pass
    else:
        print("is_valid_password should return True if it's the right password")
    if not u.is_valid_password("wrongPassword"):
        pass
    else:
        print("is_valid_password should return False if it's the wrong password")
    if not u.is_valid_password(None):
        pass
    else:
        print("is_valid_password should return False if pwd is None")

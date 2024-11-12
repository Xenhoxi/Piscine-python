from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract method for a character"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of class character"""
        self.first_name = first_name
        if is_alive is bool:
            self.is_alive = is_alive
        else:
            self.is_alive = True

    def die(self):
        """Method to kill the character"""
        if self.is_alive:
            self.is_alive = False


class Stark(Character):
    """The stark class"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of class stark"""
        super().__init__(first_name, is_alive)

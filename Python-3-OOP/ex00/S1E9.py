
from abc import ABC, abstractmethod


class Character(ABC):
    """Character abstract class that represents a character in a story."""

    def __init__(self, name: str, is_alive: bool = True) -> None:
        """Init method that initializes the name and is_alive attributes"""
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Method that sets the is_alive attribute to False"""
        self.is_alive = False


class Stark(Character):
    """Herited class from Character"""

    def die(self) -> None:
        """Method that sets the is_alive attribute to False"""
        super().die()

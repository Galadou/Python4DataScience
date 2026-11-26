from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, name: str, is_alive: bool = True) -> None:
        """Initialize the Baratheon family."""
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """Returns a readable string representation of the Baratheon family."""
        return self.__repr__()

    def __repr__(self) -> str:
        """Return all essential information about the Baratheon family."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self) -> None:
        """Method that sets the is_alive attribute to False"""
        super().die()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, name: str, is_alive: bool = True) -> None:
        """Initialize the Lannister family."""
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """Returns a readable string representation of the Lannister family."""
        return self.__repr__()

    def __repr__(self) -> str:
        """Return all essential information about the Lannister family."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self) -> None:
        """Method that sets the is_alive attribute to False"""
        super().die()

    @classmethod
    def create_lannister(cls, name: str, is_alive: bool = True) -> "Lannister":
        """Class method to create a new Lannister instance."""
        return cls(name, is_alive)

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class that inherits from both Baratheon and Lannister families."""

    def __init__(self, name: str, is_alive: bool = True) -> None:
        """Initialize the King class."""
        super().__init__(name, is_alive)

    def set_eyes(self, eyes: str) -> None:
        """Set the eye color of the King."""
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        """Set the hair color of the King."""
        self.hairs = hairs

    def get_eyes(self) -> str:
        """Get the eye color of the King."""
        return self.eyes

    def get_hairs(self) -> str:
        """Get the hair color of the King."""
        return self.hairs

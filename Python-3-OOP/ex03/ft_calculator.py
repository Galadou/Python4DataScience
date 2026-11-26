class calculator:
    """Class that performs basic arithmetic operations on a vector
    of numbers."""

    def __init__(self, vector: list) -> None:
        """Initialize the calculator with a vector of numbers."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a number to each element of the vector and print the result."""
        self.vector = [i + object for i in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each element of the vector by a number and print
        the result."""
        self.vector = [i * object for i in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a number from each element of the vector and print
        the result."""
        self.vector = [i - object for i in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide each element of the vector by a number and print the
        result. Raises an error if division by zero is attempted."""
        if object == 0:
            print("Error: Division by zero is not allowed.")
            return
        self.vector = [i / object for i in self.vector]
        print(self.vector)

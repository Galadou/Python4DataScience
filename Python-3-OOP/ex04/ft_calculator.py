class calculator:
    """Class that performs basic arithmetic operations on a vector
    of numbers."""

    @classmethod
    def dotproduct(self, V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors and print the result."""
        result = sum(i * j for i, j in zip(V1, V2))
        print(f"Dot product is: {result}")

    @classmethod
    def add_vec(self, V1: list[float], V2: list[float]) -> None:
        """Calculate the sum of two vectors and print the result."""
        result = [i + j for i, j in zip(V1, V2)]
        print(f"Add Vector is: {result}")

    @classmethod
    def sous_vec(self, V1: list[float], V2: list[float]) -> None:
        """Calculate the difference of two vectors and print the result."""
        result = [i - j for i, j in zip(V1, V2)]
        print(f"Sous vector is: {result}")

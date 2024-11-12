class calculator:
    def __init__(self):
        pass

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Display result of the dot product from 2 vectors"""
        result = 0
        for i, u in zip(V1, V2):
            result += i * u
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Display addition of 2 vectors"""
        new_vect = []
        for i, u in zip(V1, V2):
            new_vect.append(float(i + u))
        print(f"Add Vector is: {new_vect}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Display soustraction of 2 vectors"""
        new_vect = []
        for i, u in zip(V1, V2):
            new_vect.append(float(i - u))
        print(f"Sous Vector is: {new_vect}")

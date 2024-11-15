from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name):
        """Construcor of the king"""
        super().__init__(first_name)

    def set_eyes(self, new_eyes):
        """Change king's eyes color"""
        self.eyes = new_eyes

    def set_hairs(self, new_hairs):
        """Change king's hairs color"""
        self.hairs = new_hairs

    def get_eyes(self):
        """Retrieve king's eyes color"""
        return self.eyes

    def get_hairs(self):
        """Retrieve king's hairs color"""
        return self.hairs

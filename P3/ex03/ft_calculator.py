class calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object):
        """Overload + operator, add a scalar to a vector"""
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object):
        """Overload / operator, multiply a vector by a scalar"""
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object):
        """Overload - operator, soustract a scalar to a vector"""
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object):
        """Overload / operator, divide a vector by a scalar"""
        if (object == 0):
            print("Error imposible to divide by 0")
        for i in range(len(self.vector)):
            self.vector[i] /= object
        print(self.vector)

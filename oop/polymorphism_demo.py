import math

class Shape:
    def area(self):
        """Raises an error, as this method should be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override the area method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initializes a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initializes a Circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * (self.radius ** 2)

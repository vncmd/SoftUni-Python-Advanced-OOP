class ImageArea:
    def __init__(self, width: [int, float], height: [int, float]):
        self.width = width
        self.height = height

    def get_area(self) -> int or float:
        return self.width * self.height

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self) -> str:
        return f"{self.name} is {'' if self.is_happy else 'not '}happy"

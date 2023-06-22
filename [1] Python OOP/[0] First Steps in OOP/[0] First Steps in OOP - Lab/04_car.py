class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


mercedes = Car("Mercedes", "CLK GTR", "6.0L V12")
pagani = Car("Pagani", "Zonda Cinque Roadster", "7.3L V12")
koenigsegg = Car("Koenigsegg", "One:1", "5.0L V8")


print(mercedes.get_info())
print(pagani.get_info())
print(koenigsegg.get_info())

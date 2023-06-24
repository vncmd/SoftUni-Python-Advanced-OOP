class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int) -> str:
        if self.content + ml > Glass.capacity:
            return f"Cannot add {ml} ml"

        self.content += ml

        return f"Glass filled with {ml} ml"

    def empty(self) -> str:
        self.content = 0

        return "Glass is now empty"

    def info(self) -> str:
        left_capacity = Glass.capacity - self.content

        return f"{left_capacity} ml left"

# Tests:


glass = Glass()

print(glass.fill(100))
print(glass.fill(200))

print(glass.empty())
print(glass.fill(200))
print(glass.info())

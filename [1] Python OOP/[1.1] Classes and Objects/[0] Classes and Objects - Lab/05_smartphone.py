class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps = []
        self.power_on = False

    def power(self) -> None:
        self.power_on = not self.power_on

    def install(self, app: str, app_memory: int):
        if not self.power_on:
            return f"Turn on your phone to install {app}"

        if self.memory > app_memory:
            self.memory -= app_memory
            self.apps.append(app)

            return f"Installing {app}"

        return f"Not enough memory to install {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


# Tests:


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))

smartphone.power()

print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())

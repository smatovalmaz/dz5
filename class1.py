class Hello:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


class NewHello(Hello):
    def __init__(self, name):
        super().__init__(name)


    def greet_twice(self):
        return f"{self.greet()} {self.greet()}"
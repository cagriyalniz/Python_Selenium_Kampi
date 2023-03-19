class Human:
    def __init__(self, name):#construction
        self.name = name
        print("__init__ function: a human instance")
    def __str__(self):
        return f"__str__ function: {self.name}"
    def talk(self, sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking...")

human1 = Human("")
human1.name = "cagri"
human1.talk("hello world")
human1.__str__()
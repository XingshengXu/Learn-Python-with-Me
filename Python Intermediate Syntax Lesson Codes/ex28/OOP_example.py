class Mammal:
    def __init__(self, name, diet, fur_color):
        self.name = name
        self.diet = diet
        self.fur_color = fur_color

    def make_sound(self):
        return "Generic Mammal Sound"

    def walk(self):
        return f"{self.name} is walking."


class Lion(Mammal):
    def __init__(self, name, diet, fur_color, mane_color):
        super().__init__(name, diet, fur_color)
        self.mane_color = mane_color

    def hunt(self):
        return f"{self.name} is hunting."


class Bird:
    def __init__(self, name, diet, feather_color):
        self.name = name
        self.diet = diet
        self.feather_color = feather_color

    def make_sound(self):
        return "Chirp"

    def fly(self):
        return f"{self.name} is flying."


class Parrot(Bird):
    def __init__(self, name, diet, feather_color, vocab_size):
        super().__init__(name, diet, feather_color)
        self.vocab_size = vocab_size

    def talk(self):
        return f"{self.name} is talking."


class Fish:
    def __init__(self, name, diet, scale_color):
        self.name = name
        self.diet = diet
        self.scale_color = scale_color

    def make_sound(self):
        return "Glub"

    def swim(self):
        return f"{self.name} is swimming."


class Shark(Fish):
    def __init__(self, name, diet, scale_color, fin_size):
        super().__init__(name, diet, scale_color)
        self.fin_size = fin_size

    def hunt(self):
        return f"{self.name} is hunting."


# Testing Code
if __name__ == "__main__":
    simba = Lion("Simba", "Carnivore", "Brown", "Dark Brown")
    print(simba.make_sound())
    print(simba.walk())
    print(simba.hunt())

    polly = Parrot("Polly", "Herbivore", "Green", 50)
    print(polly.make_sound())
    print(polly.fly())
    print(polly.talk())

    jaws = Shark("Jaws", "Carnivore", "Gray", "Large")
    print(jaws.make_sound())
    print(jaws.swim())
    print(jaws.hunt())

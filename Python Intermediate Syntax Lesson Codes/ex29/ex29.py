# 类的变量 (Class Variables)
class Mammal:
    class_name = 'Mammalia'
    warm_blooded = True

    # @classmethod
    # def print_class_name(cls):
    #     return f"Class name is called: {cls.class_name}"

    # @classmethod
    # def from_birth_year(cls, name, birth_year):
    #     age = 2023 - birth_year
    #     return cls(name, age)

    # @staticmethod
    # def introduction():
    #     print("Mammals are a class of warm-blooded vertebrates that "
    #           "have hair or fur, and three middle ear bones.")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed(self):
        print("Feeding")

    # def __repr__(self):
    #     return f"Mammal(name='{self.name}', age={self.age})"

    # def __str__(self):
    #     return f"{self.name}, a {self.age}-year-old mammal."

    def __add__(self, other):
        if isinstance(other, Mammal):
            return Mammal(name=f"{self.name}-{other.name}",
                          age=max(self.age, other.age),)
        else:
            pass


class Dog(Mammal):
    # def __init__(self, name, age, species_name):
    #     super().__init__(name, age)
    #     self.species_name = species_name

    def bark(self):
        print("Barking")


class Cat(Mammal):
    def mewo(self):
        print("Mewoing")


# dog = Dog(name='大圣', age=5)
# cat = Cat(name='南瓜', age=8)
# print(Mammal.class_name, Mammal.warm_blooded)
# print(help(Mammal))
# print(help(Dog))

# 类的方法 (Class Methods)
# Mammal.print_class_name()

# 使用默认构建器
# mammal1 = Mammal("Tom", 3)

# 使用替代构建器
# mammal2 = Mammal.from_birth_year("Jerry", 2015)
# print(f"{mammal1.name} is {mammal1.age} years old.")
# print(f"{mammal2.name} is {mammal2.age} years old.")

# 静态方法 (Static Method)
# Mammal.introduction()

# 特殊的方法 (Dunder Methods)
# print(repr(dog))  # This will call leo.__repr__()
# print(dog)  # This will call leo.__str__()

# 特殊方法 __add__ (多态性 Polymorphism)
# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))

# mammal1 = Dog(name='大圣', age=5)
# mammal2 = Cat(name='南瓜', age=8)
# new_mammal = mammal1 + mammal2
# print(new_mammal.name, new_mammal.age)

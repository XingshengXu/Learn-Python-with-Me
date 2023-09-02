# 类的变量 (Class Variables)
class Mammal:
    class_name = 'Mammalia'
    warm_blood = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2023 - birth_year
        return cls(name, age)

    @classmethod
    def print_class_name(cls):
        return f"Class name is called: {cls.class_name}."

    @staticmethod
    def introduction():
        print("Mammals are a class of warm-blooded vertebrates that "
              "have hair or fur, and three middle ear bones.")

    def feed(self):
        print("Feeding")

    def __repr__(self):
        return f"Mammal(name='{self.name}', age={self.age})"

    def __str__(self):
        return f"{self.name}, a {self.age}-year-old mammal."

    def __add__(self, other):
        if isinstance(other, Mammal):
            return Mammal(name=f"{self.name}-{other.name}",
                          age=max(self.age, other.age),)
        else:
            pass


class Dog(Mammal):
    dog_class_name = 'Dog'

    def __init__(self, name, age, type_name):
        super().__init__(name, age)
        self.type_name = type_name

    def bark(self):
        print("Barking")


class Cat(Mammal):
    def mewo(self):
        print("Mewoing")


# dog = Dog(name='max', age=5, type_name='dog')
# cat = Cat(name='pumpkin', age=8)
# print(dog.type_name)
# print(dog.dog_class_name)
# print(dog.class_name)

# print(Mammal.class_name, Mammal.warm_blood)
# print(help(Mammal))
# print(help(Dog))

# 类的方法 (Class Methods)
# print(Mammal.print_class_name())

# 使用默认构建器
# mammal1 = Mammal("Tom", 3)

# 使用替代构建器
# mammal2 = Mammal.from_birth_year("Jerry", 2015)
# print(f"{mammal1.name} is {mammal1.age} years old.")
# print(f"{mammal2.name} is {mammal2.age} years old.")

# 静态方法 (Static Method)
# Mammal.introduction()

# 特殊的方法 (Dunder Methods)
# dog = Dog(name='max', age=5, type_name='dog')
# print(repr(dog))  # This will call dog.__repr__()
# print(dog)  # This will call dog.__str__()

# 特殊方法 __add__ (多态性 Polymorphism)
# print(int.__add__(1, 2))
# print(1+2)
# print(str.__add__('a', 'b'))
# print('a'+'b')

# mammal1 = Dog(name='max', age=5, type_name='dog')
# mammal2 = Cat(name='pumpkin', age=8)
# new_mammal = mammal1 + mammal2
# print(new_mammal.name, new_mammal.age)

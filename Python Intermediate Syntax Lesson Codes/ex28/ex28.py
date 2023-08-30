# 创建简单类
class Mammal:
    def feed(self):
        print("Feeding")

    def move(self):
        print("Moving")


# mammal1 = Mammal()
# mammal1.feed()
# mammal1.move()
# print(mammal1)

# mammal1.name = 'lion'
# print(mammal1.name)

# 类构建器 (封装性 Encapsulation)


# class Mammal:
#     def __init__(self, _name, _age):
#         self.name = _name
#         self.age = _age


# mammal1 = Mammal(_name='lion', _age=5)
# mammal2 = Mammal(_name='dog', _age=2)
# print(mammal1.name, mammal2.name)
# print(mammal1.age, mammal2.age)

# Quiz


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f'Hi, I am {self.name}.')


# hongtu = Person('HongTu')
# print(hongtu.name)
# hongtu.talk()

# 两个类的代码
# class Mammal:
#     def feed(self):
#         print("Feeding")


# class Dog:
#     def feed(self):
#         print("Feeding")

# 类的继承性 (Inheritance)
# class Mammal:  # parent class
#     def feed(self):
#         print("Feeding")


# class Dog(Mammal):  # child class/sub-class
#     def bark(self):
#         print("Barking")


# class Cat(Mammal):  # child class/sub-class
#     def mewo(self):
#         print("Mewoing")


# dog = Dog()
# cat = Cat()
# dog.feed()
# cat.feed()
# dog.bark()
# cat.mewo()

# 想要了解更多咱们这个Mammal类的结构
# print(help(Mammal))

# 查看是否是子类
# print(issubclass(Dog, Mammal))

# 查看是否是实例
# print(isinstance(dog, Dog))

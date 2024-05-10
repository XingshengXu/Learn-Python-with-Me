class Duck:

    def quack(self):
        print("嘎！嘎！")

    def fly(self):
        print("噗！噗！")


class Person:

    def quack(self):
        print("我在学鸭叫!")

    def fly(self):
        print("我在扑腾手臂飞行！")


def quack_and_fly(thing):
    # LBYL写法
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()

    # EAFP写法
    # try:
    #     thing.quack()
    #     thing.fly()
    #     # thing.bark()
    # except AttributeError as e:
    #     print(e)


duck = Duck()
person = Person()
quack_and_fly(duck)
quack_and_fly(person)

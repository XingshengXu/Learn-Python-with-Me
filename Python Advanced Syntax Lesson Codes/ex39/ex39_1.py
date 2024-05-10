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
    # 非Duck-Typed写法
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print("这不是一只鸭子！")

    # Duck-Typed写法
    # thing.quack()
    # thing.fly()


duck = Duck()
person = Person()
quack_and_fly(duck)
quack_and_fly(person)

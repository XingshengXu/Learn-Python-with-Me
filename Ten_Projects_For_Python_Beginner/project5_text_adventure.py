import random


def start_adventure():
    print("🌴 你在一座神秘的荒岛上醒来...")
    print("记忆模糊，只记得一场海难，只有你幸存。")
    print("你现在有两个选择：")
    print("1. 进入森林")
    print("2. 走向海岸")

    choice1 = input("请选择 (1 或 2): ")

    if choice1 == "1":
        enter_forest()
    elif choice1 == "2":
        go_to_coast()
    else:
        print("你站在原地发呆，最终被野兽发现并吃掉了。游戏结束。")


def enter_forest():
    print("\n🌲 你踏入茂密的森林...")
    print("突然，身后传来奇怪的声音！")

    action1 = input("你要 (a) 躲藏 还是 (b) 转身查看? ")

    if action1 == "a":
        print("你屏住呼吸躲在树后...")
        print("但一个高大的黑影出现！它居然是...")
        print("🤖 一台废弃的机器人！")
        robot_encounter()
    elif action1 == "b":
        print("你转身发现一只饥饿的老虎！")
        action2 = input("你要 (a) 冲上树 还是 (b) 用木棍防御? ")

        if action2 == "a":
            print("你快速爬上树，老虎在树下徘徊。")
            print("🌳 你发现树上有一个奇怪的宝箱！")
            open_treasure()
        elif action2 == "b":
            print("老虎被你的勇气震慑，竟然跑走了！")
            print("你松了口气，继续深入森林...")
            mysterious_cave()
        else:
            print("你站着不动，被老虎扑倒。游戏结束。")
    else:
        print("你犹豫不决，最终被野兽发现并吃掉了。游戏结束。")


def robot_encounter():
    print("\n🤖 机器人好像已经损坏...")
    print("但它的眼睛突然闪烁！")

    choice = input("你要 (a) 试图修复它 还是 (b) 逃跑? ")

    if choice == "a":
        print("你修复了机器人，它突然说：‘主人，我在等你！’")
        print("🎉 你解锁了隐藏结局！机器人带你回到了未来世界！")
    elif choice == "b":
        print("你试图逃跑，但机器人射出激光... 游戏结束。")
    else:
        print("机器人启动了自毁程序，一起炸飞了！游戏结束。")


def open_treasure():
    print("\n💎 你打开宝箱...")
    print("里面有一张藏宝图！")

    choice = input("你要 (a) 继续寻找宝藏 还是 (b) 无视它? ")

    if choice == "a":
        print("你按照地图找到了一座隐藏的神庙...")
        print("🎉 你发现了传说中的黄金神像！你成为了岛上的统治者！")
    elif choice == "b":
        print("你觉得太麻烦了，把地图丢掉。结果，你迷路了。游戏结束。")
    else:
        print("你犹豫不决，宝箱爆炸了！游戏结束。")


def mysterious_cave():
    print("\n🕳️ 你发现了一个神秘的洞穴...")
    print("洞穴里有一盏奇怪的灯！")

    choice = input("你要 (a) 擦拭它 还是 (b) 直接离开? ")

    if choice == "a":
        print("💨 一阵烟雾中，一个精灵出现！")
        print("‘你释放了我！我可以满足你一个愿望！’")

        wish = input("你要 (a) 变得超级富有 还是 (b) 永远年轻? ")
        if wish == "a":
            print("💰 精灵赐给你无数金币！但你发现岛上没有银行...游戏结束。")
        elif wish == "b":
            print("🎉 你获得了永生，但被困在岛上...游戏结束。")
        else:
            print("精灵生气了，把你变成了一只青蛙！游戏结束。")
    elif choice == "b":
        print("你错失了千载难逢的机会，空手离开。游戏结束。")
    else:
        print("你踢了一脚灯，结果洞穴塌了！游戏结束。")


def go_to_coast():
    print("\n🌊 你来到海岸...")
    print("你看到一个小木船，还有一个神秘的漂流瓶。")

    choice = input("你要 (a) 乘船离开 还是 (b) 打开漂流瓶? ")

    if choice == "a":
        print("🚣 你划向大海...")
        print("但突然一场风暴袭来，你的船沉没了。游戏结束。")
    elif choice == "b":
        print("📜 你打开漂流瓶，发现里面是一封求救信！")

        if random.choice([True, False]):
            print("⚓ 你按照信的指示找到了一艘沉船，并发现了一批黄金！")
            print("🎉 你成为了一名传奇探险家！")
        else:
            print("你花了很久研究信件，结果发现是假的...游戏结束。")
    else:
        print("你站在海边犹豫不决，突然被海浪卷走了。游戏结束。")


if __name__ == "__main__":
    start_adventure()

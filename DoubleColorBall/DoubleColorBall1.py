import random

# 红球，蓝球号码范围
red_balls = range(1, 34)
blue_balls = range(1, 17)

# 每次抽奖的彩票数量
tickets_per_drawing = 1

# 抽奖次数
num_drawings = 156

# 总支出，收入
total_spending = 0
total_earnings = 0

# 奖项历史记录
prizes_history = {
    "一等奖": 0,
    "二等奖": 0,
    "三等奖": 0,
    "四等奖": 0,
    "五等奖": 0,
    "六等奖": 0,
    "感谢参与": 0
}

# 计算奖金的函数


def calculate_prize(my_numbers, winning_numbers):
    # 计算红球匹配数和蓝球是否匹配
    red_matches = len(my_numbers["red"] & winning_numbers["red"])
    blue_match = (my_numbers["blue"] == winning_numbers["blue"])

    # 奖金映射表
    prize_map = {
        (6, True): (700_000_000, "一等奖"),
        (6, False): (28_000_000, "二等奖"),
        (5, True): (3_000, "三等奖"),
        (5, False): (200, "四等奖"),
        (4, True): (200, "四等奖"),
        (4, False): (10, "五等奖"),
        (3, True): (10, "五等奖"),
        (2, True): (5, "六等奖"),
        (1, True): (5, "六等奖"),
        (0, True): (5, "六等奖"),
    }

    # 根据匹配结果得到奖金和类别
    if (red_matches, blue_match) in prize_map:
        prize, category = prize_map[(red_matches, blue_match)]
        prizes_history[category] += 1
    else:
        prize = 0
        prizes_history["感谢参与"] += 1

    return prize


# 购买彩票并计算结果
for _ in range(num_drawings):
    red_drawing = set(random.sample(red_balls, 6))
    blue_drawing = random.choice(blue_balls)

    drawn_numbers = {"red": red_drawing, "blue": blue_drawing}

    for _ in range(tickets_per_drawing):
        total_spending += 2

        my_red = set(random.sample(red_balls, k=6))
        my_blue = random.choice(blue_balls)

        player_numbers = {"red": my_red, "blue": my_blue}
        earning = calculate_prize(player_numbers, drawn_numbers)
        total_earnings += earning

# 打印总支出和总收入
print(f'总花费: ¥{total_spending}')
print(f'总收入: ¥{total_earnings}')
print(prizes_history)

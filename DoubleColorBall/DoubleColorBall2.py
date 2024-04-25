import random
import matplotlib.pyplot as plt

# 红球，蓝球号码范围
red_balls = range(1, 34)
blue_balls = range(1, 17)

# 每次抽奖的彩票数量
tickets_per_drawing = 100

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

# 支出和收入历史
spending_history = []
earnings_history = []
years = []

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


# 初始化中奖标志、抽奖次数和年份计数器
hit_bigprize = False
drawings = 0
year_count = 0

# 如果没有中最大奖，就继续抽奖
while not hit_bigprize:
    drawings += 1

    # 随机选取6个红球和1个蓝球
    red_drawing = set(random.sample(red_balls, 6))
    blue_drawing = random.choice(blue_balls)

    # 将抽出的号码存储为字典
    drawn_numbers = {"red": red_drawing, "blue": blue_drawing}

    # 购买彩票并计算结果
    for _ in range(tickets_per_drawing):
        total_spending += 2
        my_red = set(random.sample(red_balls, k=6))
        my_blue = random.choice(blue_balls)
        player_numbers = {"red": my_red, "blue": my_blue}
        earning = calculate_prize(player_numbers, drawn_numbers)
        total_earnings += earning

        # 如果中了最大奖，则结束循环
        # if earning == 700_000_000:
        #     hit_bigprize = True
        #     break

    # 如果有了正利润，则结束循环
    if total_earnings - total_spending > 0:
        hit_bigprize = True

    # 如果达到了一年的抽奖次数，更新年度记录
    if drawings % num_drawings == 0:
        year_count += 1
        spending_history.append(total_spending / 1e4)
        earnings_history.append(total_earnings / 1e4)
        years.append(year_count)
        print(f'{year_count} 年')


# 如果循环结束时不是在156次抽奖结束，也要记录下来
if drawings % num_drawings != 0:
    year_count += 1
    spending_history.append(total_spending / 1e4)
    earnings_history.append(total_earnings / 1e4)
    years.append(year_count)

# 绘制利润图
profits = [earn - spend for earn,
           spend in zip(earnings_history, spending_history)]
plt.figure(figsize=(10, 5))
plt.plot(years, profits, marker='o', linestyle='-', color='b')
plt.title('Double Color Ball Profit Chart')
plt.xlabel('Year')
plt.ylabel('Profit (unit: 10k RMB)')
plt.grid(True)
plt.show()

# 打印总支出和总收入
print(f'总花费: ¥{total_spending}')
print(f'总收入: ¥{total_earnings}')
print(prizes_history)

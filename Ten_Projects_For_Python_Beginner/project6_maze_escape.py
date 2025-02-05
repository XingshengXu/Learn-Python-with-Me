# 迷宫地图（0 表示路，1 表示墙）
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

player_pos = [0, 0]
exit_pos = [4, 4]


def print_maze():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if [i, j] == player_pos:
                print("P", end=" ")  # 玩家位置
            elif [i, j] == exit_pos:
                print("E", end=" ")  # 终点
            elif maze[i][j] == 1:
                print("#", end=" ")  # 墙壁
            else:
                print(".", end=" ")  # 空地
        print()
    print()


def move_player(direction):
    x, y = player_pos
    if direction == "w" and x > 0 and maze[x - 1][y] == 0:
        player_pos[0] -= 1
    elif direction == "s" and x < len(maze) - 1 and maze[x + 1][y] == 0:
        player_pos[0] += 1
    elif direction == "a" and y > 0 and maze[x][y - 1] == 0:
        player_pos[1] -= 1
    elif direction == "d" and y < len(maze[0]) - 1 and maze[x][y + 1] == 0:
        player_pos[1] += 1
    else:
        print("不能走那边！")


while player_pos != exit_pos:
    print_maze()
    move = input("输入 w/a/s/d 移动 (w=上, a=左, s=下, d=右): ").lower()
    move_player(move)

print("恭喜！你成功逃出迷宫！")

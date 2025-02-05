import random


def print_board(board):
    """打印棋盘"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """检查是否有玩家获胜"""
    # 检查行
    for row in board:
        if all(cell == player for cell in row):
            return True

    # 检查列
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # 检查对角线
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    """检查棋盘是否已满"""
    return all(cell in ('X', 'O') for row in board for cell in row)


def computer_move(board):
    """电脑随机选择一个空位"""
    empty_cells = [(r, c) for r in range(3)
                   for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_cells)


def tic_tac_toe():
    """运行井字棋游戏，玩家 vs 电脑"""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    computer = 'O'

    while True:
        print_board(board)

        if (sum(row.count(' ') for row in board)) % 2 == 1:  # 玩家回合
            print("轮到玩家 X 走")
            while True:
                try:
                    row, col = map(int, input("请输入行和列(0-2), 用空格分隔: ").split())
                    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                        board[row][col] = player
                        break
                    else:
                        print("无效输入，请输入未被占用的位置(0-2)。")
                except ValueError:
                    print("输入格式错误, 请输入两个0到2之间的数字, 并用空格分隔。")
        else:
            print("轮到电脑 O 走")
            row, col = computer_move(board)
            board[row][col] = computer

        if check_winner(board, player):
            print_board(board)
            print("玩家 X 获胜！")
            break

        if check_winner(board, computer):
            print_board(board)
            print("电脑 O 获胜！")
            break

        if is_full(board):
            print_board(board)
            print("平局！")
            break


if __name__ == "__main__":
    tic_tac_toe()

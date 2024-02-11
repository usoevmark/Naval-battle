import random

# Функция для создания игрового поля
def create_board():
    board = []
    for _ in range(5):
        board.append(["O"] * 5)
    return board

# Функция для отображения игрового поля
def print_board(board):
    for row in board:
        print(" ".join(row))

# Функция для случайного размещения кораблей
def place_ships(board):
    for _ in range(3):
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        board[row][col] = "X"

# Функция для проверки попадания
def check_hit(board, guess_row, guess_col):
    if board[guess_row][guess_col] == "X":
        print("Поздравляем! Вы попали в корабль!")
        board[guess_row][guess_col] = "*"
    else:
        print("Увы! Вы промахнулись!")
        board[guess_row][guess_col] = "!"

# Основная функция игры
def main():
    print("Добро пожаловать в игру 'Морской бой'!")
    print("Попробуйте потопить три корабля!")
    print()
    board = create_board()
    place_ships(board)
    # Для отладки: раскомментируйте строку ниже, чтобы увидеть расположение кораблей
    # print_board(board)
    print()
    print_board(board)
    print()
    for turn in range(10):
        print(f"Ход {turn + 1}")
        guess_row = int(input("Введите номер строки (от 0 до 4): "))
        guess_col = int(input("Введите номер столбца (от 0 до 4): "))
        if guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
            print("Вы ввели недопустимое значение!")
            continue
        check_hit(board, guess_row, guess_col)
        print_board(board)
        print()
        if sum(row.count("*") for row in board) == 3:
            print("Поздравляем! Вы потопили все корабли!")
            break
    else:
        print("К сожалению, у вас закончились ходы. Игра окончена.")

if __name__ == "__main__":
    main()

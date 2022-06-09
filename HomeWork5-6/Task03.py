# Создайте программу для игры в "Крестики-нолики"


def print_field(maxtrix):
    print("Field")
    print("---------------")
    for i in range(3):
        field = []
        for j in range(3):
            value = maxtrix[i][j]
            if value == 0:
                field.append("-")
            elif value == 1:
                field.append("X")
            else:
                field.append("O")
        print(field)
    print("---------------")


def input_coords(matrix):
    while True:
        coords = input()
        try:
            oX = int(coords[:1]) - 1
            oY = int(coords[1:]) - 1
            if oX > 2 or oX < 0 or oY > 2 or oY < 0:
                print("Incorrect data. Retype.")
                continue
            elif matrix[oX][oY] != 0:
                print("This cell is occupied, please select another")
                continue               
            break
        except ValueError:
            print("Incorrect data. Retype.")
        # except KeyboardInterrupt:
        #     print("Фигня какая то, повторите ввод =)")
    return (oX, oY)


def winner_check(matrix):
    # Проверка Диагоналей
    # Так как у нас всегда стандартное поле 3х3 то проще подсчитать напрямую элементы по индексам
    main_diag = matrix[0][0] + matrix[1][1] + matrix[2][2]
    secondary_diag = matrix[2][0] + matrix[1][1] + matrix[0][2]
    if (main_diag == 3 or secondary_diag == 3) or (main_diag == -3 or secondary_diag == -3):        
        return True

    # Проверка горизонательных и вертикальных линий
    for i in range(3):
        hori_sum = matrix[i][0] + matrix[i][1] + matrix[i][2]
        vert_sum = matrix[0][i] + matrix[1][i] + matrix[2][i]
        if (hori_sum == 3 or vert_sum == 3) or (hori_sum == -3 or vert_sum == -3):            
            return True
    return False


def repeat_game():
    print("Want to play more? ( Press 1 - Play again, anykey - Quit)")
    answer = input()
    return True if answer == "1" else False


def tictactoe() -> None:
    field = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print("\nWelcome to the game!\n")
    print_field(field)
    count_turns = 0
    while True:
        count_turns += 1
        flag = count_turns % 2
        number_player = 1 if flag else 2
        print(f"Player {number_player} your turn. Enter the line number and column number together. From 1 to 3")
        oX, oY = input_coords(field)

        # Крестик = 1, Нолик = -1
        field[oX][oY] = 1 if flag else -1
        print_field(field)        
        
        if winner_check(field):
            print(f"Player {number_player} won")
            if repeat_game():
                count_turns = 0
                field = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
                print_field(field)
            else:
                print("Goodbye. Come again")
                return

        # Если все ячейки поля заняты
        if count_turns == 9:
            print("Fighting draw.")
            if repeat_game():
                count_turns = 0
                field = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
                print_field(field)
            else:
                print("Goodbye. Come again")
                return

#Start game
tictactoe()


# Проект игры Крестики-Нолики

M = 3  # Размер игрового поля (квадрат со стороной M)
VOID_CELL_SYMB = '-'  # Символ незанятой ячейки
VALUE_X = 'X'  # Символ игрока X
VALUE_0 = '0'  # Символ игрока 0
EXIT_STRING = "exit"

game_table = None  # Игровое поле
flag_exit = None  # Флаг запроса на выход из игры

def main():

    winner_name = ""

    # инициализация
    init(M)

    # Приветствие
    hello()

    # Показываем исходное игровое поле
    show_status()

    for x in range(1, M * M + 1):
        if x % 2:
            move_gamer(VALUE_X)
        else:
            move_gamer(VALUE_0)

        show_status()

        winner_name = is_game_over()

        if winner_name or flag_exit:
            break

    show_game_result(winner_name)
    show_status()


def init(game_table_size):

    global game_table
    global VALUE_X
    global VALUE_0

    game_table = [[VOID_CELL_SYMB for a in range(game_table_size)] for b in range(game_table_size)]


def hello():

    print('Добро пожаловать в игру "Крестики-нолики"')
    print("Первый ход за игроком X! Игра начинается!\n")


def show_status():

    str_ = ''

    for x in range(len(game_table)):
        str_ += '\t' + str(x)
    print(str_)

    i = 0
    for y in game_table:
        str_ = ''
        for x in y:
            str_ += '\t' + x
        print(str(i) + str_)
        i += 1


def update_status(symb):
    global flag_exit
    addr = []

    lst = str.split(input("Введите координаты ячейки (горизонталь и вертикаль через пробел). Если хотите выйти из игры, введите " + EXIT_STRING + ".\nВводите:"))

    if len(lst) == 1 and lst.count(EXIT_STRING) == 1:
        flag_exit = True
    else:
        for val in lst:
            if str.isdigit(val):
                addr.append(int(val))

        if len(addr) == 2:
            if (0 <= addr[0] < M) and (0 <= addr[1] < M):
                if game_table[addr[0]][addr[1]] is VOID_CELL_SYMB:
                    game_table[addr[0]][addr[1]] = symb
                    return True
                else:
                    print("Ячейка с координатами " + str(addr) + " уже заполнена")
            else:
                print("Координаты " + str(addr) + " выходят за пределы игрового поля")
        else:
            print("Ошибка ввода адреса ячейки")

    return False


def is_game_over():

    check_horizontal = check_winner_horizontal()

    if check_horizontal:
        return check_horizontal
    else:
        check_vertical = check_winner_vertical()

        if check_vertical:
            return check_vertical
        else:
            return check_winner_diagonal()


def show_game_result(winner_name):

    print("=" * 30)
    print("Игра окончена!")

    if winner_name:
        print("Победил игрок " + str.upper(winner_name))
    else:
        print("Результат игры: ничья!")


def move_gamer(gamer_name):

    global flag_exit

    print("+" * 15)
    print("Ходит игрок ", gamer_name)

    while True:
        if update_status(str.upper(gamer_name)) or flag_exit:
            break

    print("Ход игрока " + gamer_name + " сделан")
    print("-" * 15)


def check_winner_horizontal():

    # последовательно проверяем все строки
    for y in game_table:
        sign = check_item_to_winner_sign(y)
        if sign:
            return sign
    return None


# функция проверяет, есть ли в списке признак победы одного из игроков
def check_item_to_winner_sign(lst):

    # если все поле заполнено ходами игроков ...
    if not set(lst).intersection(set(list(VOID_CELL_SYMB))):
        # lst_x содержит список пересечения с символом игрока X
        lst_x = list(set(list(map(str, lst))).intersection(list(VALUE_X)))

        # lst_0 содержит список пересечения с символом игрока 0
        lst_0 = list(set(list(map(str, lst))).intersection(list(VALUE_0)))

        # ...и во всей выборке нет ходов игрока X, то все ходы в выборке принадлежат игроку 0 (победа игрока 0)
        if not len(lst_x):
            return VALUE_0

        if not len(lst_0):
            return VALUE_X

    return None


def check_winner_vertical():

    lst = []
    for x in range(M):
        for y in game_table:
            if len(y) > x:
                lst.append(y[x])

        sign = check_item_to_winner_sign(lst)
        lst.clear()
        if sign:
            return sign


def check_winner_diagonal():

    lst_diag1 = []
    lst_diag2 = []
    for i in range(M):
        lst_diag1.append(game_table[i][i])
        lst_diag2.append(game_table[M - 1 - i][i])

    sign = check_item_to_winner_sign(lst_diag1)
    if not sign:
        return check_item_to_winner_sign(lst_diag2)
    else:
        return sign


if __name__ == "__main__":
    main()

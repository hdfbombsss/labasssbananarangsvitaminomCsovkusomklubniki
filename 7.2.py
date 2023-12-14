import random
import sys


def create_matrix ( ):
    while True:
        try:
            rows = int (input ("Введите количество строк матрицы: "))
            columns = int (input ("Введите количество столбцов матрицы: "))
            if rows < 0 or columns < 0:
                raise ValueError
            break
        except ValueError:
            print ("Количество строк и столбцов должны быть неотрицательными целыми числами")

    matrix = [ ]
    generate_random = input (
        "Хотите сгенерировать матрицу случайно? (Введите 'да', если хотите сгенерировать случайно, иначе 'нет' и вводите сами): ")

    if generate_random == "да":
        for i in range (rows):
            row = [ ]
            for j in range (columns):
                row.append (random.randint (0, 100))
            matrix.append (row)
    elif generate_random == "нет":
        for i in range (rows):
            row = [ ]
            for j in range (columns):
                while True:
                    try:
                        num = float (input (f"Введите значение элемента под номером [{i}][{j}]: "))
                        row.append (num)
                        break
                    except ValueError:
                        print ("Введите число!")
            matrix.append (row)
    else:
        print (
            "Поздравляю вас, вы не умеете читать. Надеюсь, вы прочитаете этот текст и перезапустите программу заново. Император вами недоволен -300 социальных кредитов")
        sys.exit ()

    return matrix


def shift_list ( lst, n, direction ):
    if direction == "right":
        n = n % len (lst)
        return lst [ -n: ]+lst [ :-n ]
    elif direction == "down":
        n = n % len (lst)
        return lst [ -n: ]+lst [ :-n ]
    else:
        print ("Неверный режим. Режим должен быть 'right' или 'down'")
        return None


matrix = create_matrix ()

while True:
    try:
        n = int (input ("Введите количество элементов для сдвига: "))
        if n < 0:
            raise ValueError
        break
    except ValueError:
        print ("Количество элементов сдвига должно быть неотрицательным целым числом")

while True:
    direction = input ("Введите режим сдвига ('right' или 'down'): ")
    if direction == "right" or direction == "down":
        break
    else:
        print ("Неверный режим. Режим должен быть 'right' или 'down'")

new_matrix = [ ]
if direction == "right":
    for i in range (len (matrix)):
        new_row = shift_list (matrix [ i ], n, "right")
        new_matrix.append (new_row)
elif direction == "down":
    for j in range (len (matrix [ 0 ])):
        column = [ matrix [ i ] [ j ] for i in range (len (matrix)) ]
        new_column = shift_list (column, n, "down")
        new_row = [ new_column [ i ] for i in range (len (matrix)) ]
        new_matrix.append (new_row)
else:
    print ("Неверный режим. Режим должен быть 'right' или 'down'")
    new_matrix = None

if new_matrix is not None:
    print ("Исходная матрица:")
    for row in matrix:
        print (row)

    print ("Матрица после сдвига:")
    for row in new_matrix:
        print (row)


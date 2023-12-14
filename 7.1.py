import random, sys

def create_matrix():
    while True:
        try:
            M = int(input("Введите число строк: "))
            N = int(input("Введите число столбцов: "))
            if M > 0 and N > 0:
                break
            else:
                print("Введите целое положительное число!")
        except ValueError:
            print("Введите целое число!")

    matrix = []

    generate_random = input("Хотите сгенерировать матрицу случайно? (введите да если хотите сгенерировать случайно иначе нет и вводите сами): ")
    if generate_random == "да":
        for i in range(M):
            row = []
            for j in range(N):
                row.append(random.randint(0, 9))
            matrix.append(row)
    elif generate_random == "нет":
        for i in range(M):
            row = []
            for j in range(N):
                while True:
                    try:
                        num = float(input(f"Введите значение элемента под номером [{i}][{j}]: "))
                        row.append(num)
                        break
                    except ValueError:
                        print("Введите целое число!")
            matrix.append(row)
    else:
        print("Поздравляю вас вы не умеете читать.Надеюсь вы прочитаете этот текст и перезапустите программу заново. Император вами недоволен -300 social credit")
        exit()

    return matrix

def find_min_element(matrix):
    min_element = matrix[0][0]
    min_i = 0
    min_j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]
                min_i = i
                min_j = j

    return min_i, min_j

def remove_row_and_column(matrix, i, j):

    new_matrix = []

    for x in range(len(matrix)):
        if x != i:
            new_row = []
            for y in range(len(matrix[x])):
                if y != j:
                    new_row.append(matrix[x][y])
            new_matrix.append(new_row)

    return new_matrix

def print_matrix(matrix):

    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


matrix = create_matrix()

print("Матрица до:")
print_matrix(matrix)

min_i, min_j = find_min_element(matrix)
new_matrix = remove_row_and_column(matrix, min_i, min_j)

print("Матрица после:")
print_matrix(new_matrix)
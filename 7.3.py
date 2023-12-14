import random

def create_dict_from_string(s):
    dictionary = {}
    for char in s:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

def generate_random_dict():
    characters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ0123456789!#$%&()*+, -./:;<=>?@[\]^_`{|}~'
    while True:
        try:
            num_chars = int(input("Введите количество символов для генерации: "))
            if num_chars < 0:
                print("Пожалуйста, введите неотрицательное число.")
            else:
                break
        except ValueError:
            print("Пожалуйста, введите целое неотрицательное число.")
    dictionary = {}
    for _ in range(num_chars):
        char = random.choice(characters)
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    print("Сгенерированный словарь:", dictionary)


def get_user_choice():
    while True:
        choice = input("Хотите сгенерировать случайный словарь? (да/нет): ")
        if choice.lower() == 'да':
            return True
        elif choice.lower() == 'нет':
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

choice_random = get_user_choice()
if choice_random:
    result_dict = generate_random_dict()
else:
    s = input("Введите строку: ")
    result_dict = create_dict_from_string(s)
    print("Словарь:", result_dict)


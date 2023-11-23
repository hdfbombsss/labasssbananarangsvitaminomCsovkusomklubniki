import string

def count_double_consonants(text):
    double_consonants = 0
    for i in range(len(text) - 1):
        if text[i] in string.ascii_lowercase and text[i] != 'e' and text[i] != 'i' and text[i] != 'o' and text[i] != 'u'and text[i] not in ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']:
            if text[i] == text[i+1]:
                double_consonants += 1
    return double_consonants

while True:
    try:
        text = input("Введите текст: ")
        double_consonants = count_double_consonants(text)
        print(f"Количество двойных согласных в тексте: {double_consonants}")
        break
    except ValueError as e:
        print(f"Ошибка: {e}")

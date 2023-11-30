alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л',
            'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш',
            'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
            'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
            'и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]


def count_double_consonants(text):
    double_consonants = 0
    for i in range(len(text) - 1):
        if text[i] in alphabet and text[i] != 'e' and text[i] != 'i' and text[i] != 'o' and text[i] != 'u'and text[i] not in ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']:
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

alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л',
            'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш',
            'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
            'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
            'и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

def count_words(text):
    word_count = 0
    has_words = False
    for char in text:
        if char in alphabet:
            has_words = True
        elif char not in alphabet and has_words:
            word_count += 1
            has_words = False
    if has_words:
        word_count += 1
    if word_count == 0:
        raise ValueError("Ошибка введенный текст не соддержит слов.")

    return word_count

while True:
    try:
        text = input("Enter a text: ")
        word_count = count_words(text)
        print(f"Количество слов: {word_count}")
        break
    except ValueError as e:
        print(f"Ошибка: Введенное значение не является словом.")
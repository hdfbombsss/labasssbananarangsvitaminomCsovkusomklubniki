import string

def count_words(text):
    word_count = 0
    has_words = False

    for char in text:
        if char.lower() in string.ascii_lowercase:
            has_words = True
        elif char.lower() not in string.ascii_lowercase and has_words:
            word_count += 1
            has_words = False

    if has_words:
        word_count += 1

    if word_count == 0:
        raise ValueError("Input text does not contain any words.")

    return word_count
while True:
    try:
            text = input("Enter a text: ")
            word_count = count_words(text)
            print(f"The number of words in the text is: {word_count}")
            break
    except ValueError as e:
        print(f"Error: {e}")
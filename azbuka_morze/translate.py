import azbukamorze

def main():
    show_choice()

def show_choice():
    """Меню"""
    choice = None
    while choice != "0":
        print(
            "
            'Меню:',
            '0 - Выход.',
            '1 - Перевести слово или предложение на азбуку.',
            '2 - Перевести азбуку в символ или слово/предложение.',
            sep='\n'
            "
        )
        choice = input("\nВаш выбор - ")
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            translate_words_in_morze()
        elif choice == "2":
            translate_morze_in_words()


def translate_words_in_morze():
    """Переводит слова в азубку морзе."""
    code = ''
    words = input("Введите слово или предложение: ")
    AM = azbukamorze.AzbukaMorze(words)
    for l in AM.get_string().lower():
        if l in AM.dict_az_morze():
            code += AM.dict_az_morze()[l].replace(' ', '') + " "
    print(code)


def translate_morze_in_words():
    """Перевожу код азбуки в обратно в текст."""
    word = ""
    code = input("Код для расшифровки: ").split()
    AM = azbukamorze.AzbukaMorze(code)
    for c in code:
        for k, v in AM.dict_az_morze().items():
            if v == c:
                word += k + ' '
    print(f"Расшифровываю, это - {word}")

main()

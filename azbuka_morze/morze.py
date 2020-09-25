class AzbukaMorze():
    """Класс для перевода кода морзе в текст и наоборот."""

    def __init__(self):
        """Инициализаця атрибутов"""

    def dict_morze(self):
        """Словарь с азбукой."""
        rus = {
            'а': '•-', 'б': '-•••', 'в': '•--', 'г': '--•', 'д': '-••',
            'е': '•', 'ж': '•••-', 'з': '--••', 'и': '••', 'й': '•---',
            'к': '-•-', 'л': '•-••', 'м': '--', 'н': '-•', 'о': '---',
            'п': '•--•', 'р': '•-•', 'с': '•••', 'т': '-', 'у': '••-',
            'ф': '••-•', 'х': '••••', 'ц': '-•-•', 'ч': '---•',
            'ш': '----', 'щ': '--•-', 'ъ': '--•--', 'ы': '-•--',
            'ь': '-••-', 'э': '••-••', 'ю': '••--', 'я': '•-•-',
            '0': '-----', '1': '•----', '2': '••---', '3': '•••--',
            '4': '••••-', '5': '•••••', '6': '-••••', '7': '--•••',
            '8': '---••', '9': '----•',
            '.': '••••••', ',': '•-•-•-',
            ':': '---•••', ';': '-•-•-',
            '(': '-•--•-', ')': '-•--•-',
            "'": '•----•', '"': '•-••-•',
            '—': '-••••-', '/': '-••-•',
            '?': '••--••', '!': '--••--',
            '@': '•--•-•',
        }
        return rus

    def dict_morze_text(self):
        """Конвертирую словарь morze наоборот"""
        dict_morze_text = {}
        for k, v in self.dict_morze().items():
            dict_morze_text[v] = k
        return dict_morze_text


    def show_menu(self):
        """Показывает меню"""
        print(
            """
            Меню:
            0 - Выход.
            1 - Перевести символ на азбуку
            2 - Перевести слово или предложение на азбуку
            3 - Перевести азбуку в символ
            """
              )

    def show_choice(self):
        """Меню"""
        choice = None
        while choice != "0":
            self.show_menu()
            choice = input("\nВаш выбор - ")
            if choice == "0":
                print("До свидания!")
            elif choice == "1":
                self.translate_liter_in_morze()
            elif choice == "2":
                self.translate_words_in_morze()
            elif choice == "3":
                self.translate_morze_in_words()


    def translate_liter_in_morze(self):
        """Переводит букву в сиволы для передачи по азбуке морзе."""
        litter = input("Какую букву или сивол перевести: ")
        litter = litter.lower()
        if len(litter) == 1:
            if litter in self.dict_morze():
                print(f"Символ {litter} переводится вот так: {self.dict_morze()[litter].replace(' ', '')}")
        else:
            print('Извините, но я не могу перевести больше 1 символа, выберите другой пункт в меню.')

    def translate_words_in_morze(self):
        """Переводит слова в азубку морзе."""
        code = ''
        words = input("Введите слово или предложение: ")
        for l in words.lower():
            if l in self.dict_morze():
                code += self.dict_morze()[l].replace(' ', '') + " "
        print(code)

    def translate_morze_in_words(self):
        """Перевожу код азбуки в обратно в текст."""
        word = ""
        code = input("Код для расшифровки: ")
        code = code.split()
        for c in code:
            if c in self.dict_morze_text():
                word += self.dict_morze_text()[c]
        print(f"Расшифровываю, это - {word}")

my = AzbukaMorze()
my.show_choice()

from tkinter import *


def dict_morze():
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


def dict_morze_text():
    """Конвертирую словарь morze наоборот"""
    dict_morze_text = {}
    for k, v in dict_morze().items():
        dict_morze_text[v] = k
    return dict_morze_text

def translate_words_in_morze(event):
    """Переводит слова в азубку морзе."""
    words_codes = entry1.get()
    code = ''
    for l in words_codes.lower():
        if l in dict_morze():
            code += dict_morze()[l].replace(' ', '') + " "
    rezult.insert(1.0, code)

def translate_morze_in_words(event):
    """Перевожу код азбуки в обратно в текст."""
    codes_words = entry1.get()
    word = ""
    codes_words = codes_words.split()
    for c in codes_words:
        if c in dict_morze_text():
            word += dict_morze_text()[c]
    rezult.insert(1.0, word)

def deleteText():
    rezult.delete(1.0, END)

root = Tk()
# Наименование окна
root.title("Азбука морзе 0.1")
# Размер окна
root.geometry("300x200")

# Хранение надписи "Напишите код или текст:"
frame1 = Frame(root)
frame1.pack()

# Храню строку вводу"
frame2 = Frame(root)
frame2.pack()

# Храню кнопки
frame3 = Frame(root)
frame3.pack()

# Храню результат
frame4 = Frame(root)
frame4.pack()

# Храню кнопки под результатом
frame5 = Frame(root)
frame5.pack()

# Прошу ввести что нибудь:
txt_code = Label(frame1, text="Напишите код или текст:")
txt_code.grid(row=0, column=0)

# Создаю область для ввода текста
entry1 = Entry(frame2, width=240)
entry1.grid(row=0, column=0)

# Создаю кнопки
button1 = Button(frame3, text="Код", command=translate_words_in_morze)
button1.grid(row=0, column=0)
button2 = Button(frame3, text="Текст")
button2.grid(row=0, column=1)

# Результат
rezult = Text(frame4, height=5)
rezult.grid(row=0, column=0)

# Кнопки под результатом
button3 = Button(frame5, text="Очистить", command=deleteText)
button3.grid(row=0, column=0)

# Нажатие кнопки
button1.bind("<Button-1>", translate_words_in_morze)
button2.bind("<Button-1>", translate_morze_in_words)

root.mainloop()
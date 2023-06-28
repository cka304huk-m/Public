from azbuka import *

def main():
    choice = int(input("1 - в морзе, 2 - в текст: "))
    string = input('Введите символ, слово или предложение: ')

    result = convert(choice, string)

    print(result)

def convert(choice, string):
    """Конвертация на основе выбора пользователя."""
    word = Morse()
    if choice == 1:
        string = string.upper()
        rezult = ''
        for s in string:
            if s == ' ':
                pass
            else:
                rezult += word.convertInMorse(s) + ' '
    elif choice == 2:
        string = string.upper().split()
        rezult = ''
        for s in string:
            rezult += word.convertInText(s) + ' '

    return rezult

if __name__ == '__main__':
    main()
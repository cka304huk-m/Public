# импортирую модуль для генерации таблицы.
import random

def gen_tables():
    """Тут храниться вся сгенерированная таблица"""
    tables = []
    digits = list(range(1, 11))
    for digit in digits:
        for i in range(1, 11):
            t = digit * i
            tables.append(f"{digit} * {i} = {t}")
    return tables

def instruction():
    """Инструкция"""
    print(
        """
        Программа генерирует таблицу умножения для школьников.
        
        Меню:
        
        0 - Для выхода из программы
        1 - Для вывода всей таблицы
        2 - Для вывода определенного числа
        3 - Проверь свои знания
        """
    )
def start():
    """Выбор меню"""
    choice = None
    while choice != "0":
        instruction()
        choice = input("Сделайте выбор: ")
        if choice == "0":
            print("Спасибо, за то что попробовали мою программу.")
        elif choice == "1":
            full_tables()
        elif choice == "2":
            certain_number()
        elif choice == "3":
            gen_examples()

def full_tables():
    """Показывает на экран всю таблицу."""
    tables = gen_tables()
    print(f"--- Таблица умножения ---")
    for table in tables:
        print(table)
    print()

def certain_number():
    """Указываем на какое число нужно сгенерировать таблицу."""
    choice = int(input("На какое число сгенирировать таблицу: "))
    tables = []
    digits = list(range(1, 11))
    for digit in digits:
        t = choice * digit
        tables.append(f"{choice} * {digit} = {t}")
    print(f"--- Таблица умножения c числом {choice} ---")
    for table in tables[:10]:
        print(table)
    print()

def gen_examples():
    """Проверка знаний."""
    while True:
        print("Для возврата в предыдущее меню напишите 'q'")
        example = random.choice(gen_tables())
        ex = input(f"Сколько будет? {example[:8]}")
        if ex == 'q':
            print("Приходи еще с новыми знаниями.")
            break
        if ex in example[8:]:
            print(f"Молодец! Ты прав число равно {example[8:]}")
        else:
            print(f"Учим дальше! На самом деле число {example[8:]}")

def main():
    """Функция которая хранит все необходимое для запуска программы."""
    start()

main()

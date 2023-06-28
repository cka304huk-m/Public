import random                                                   # импортирую модуль для генерации случайных значений

examples = []                                                   # пустой список с примерами.

symbols = ['+', '-', '/', '*']                                  # список символов для случайной генерации знаков.

print("Задайте 2 числа минимальное и максимальное.")
min_digit = input("Минимальное число: ")
min_digit = int(min_digit)
max_digit = input("Максимальное число: ")
max_digit = int(max_digit)
amout_examples = input("Сколько примеров нужно сгенерировать? ")
amout_examples = int(amout_examples)

while len(examples) < amout_examples:                           # повторяет цикл, пока небудет нужного кол-ва примеров..
    number_1 = random.randint(min_digit, max_digit)
    symbol = random.choice(symbols)                             # генерирует случайный символ
    number_2 = random.randint(min_digit, max_digit)
    if number_1 >= number_2:                                
        full = f"{number_1} {symbol} {number_2} ="
    else:
        full = f"{number_2} {symbol} {number_1} ="
    examples.append(full)
print("Список примеров для решения:")
for example in examples:
    print(example)

if len(examples) == 1:
    print(f"\nВсего примеров {len(examples)} штука.")
else:
    print(f"\nВсего примеров {len(examples)} штуки.")

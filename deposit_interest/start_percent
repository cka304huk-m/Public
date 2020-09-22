from back_end import DepositCalculator

while True:
    try:
        deposit = input('Сумма депозита: ')
        interest_rate = input('Годовая процентная ставка: ')
        days = input('На какой период, укажите в днях: ')
        days_year = input('Кол-во дней в году: ')

        my_percent = DepositCalculator(deposit, interest_rate, days, days_year)

    except ValueError:
        print("Вводите пожалуйста только цифры!")
        print("Начнем с начала!")
        continue
    else:
        print("\nМой доход с " + str(my_percent.my_deposit()) + ", состовляет " + str(my_percent.percent()) +
              ". \nИтого я получу за " + str(my_percent.days) + " день(дней) " + str(my_percent.all_sum()))

    repeat = input("\nПосчитать еще? Напишите 'нет' для выхода из программы: ")
    if repeat == 'нет':
        break
    else:
        continue

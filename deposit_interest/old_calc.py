import datetime # импортирую библиотеку с текщей датой.
now = datetime.datetime.today() # текущий год, месяц и день
year_n = now.year # текущий год
month_n = now.month # текущий месяц
day_n = now.day # текущий день

while True:
    days_year = input('Сколько дней в этом году, 365 - 366? ')
    happy_year = input('год рождения: ')
    happy_month = input('месяц рождения: ')
    happy_day = input('день рождения: ')

# текущий день:
    if month_n == 1 or 3 or 5 or 7 or 8 or 10 or 12: # если месяц равен 1, 3, 5, 7, 8, 10 и 12, то умножаем на 31
        year_sum = (int(year_n) * 365) + (month_n * 31) + int(day_n)
    elif month_n == 2: # если месяц равен 2, то умножаем на 28 если 365 дней в году
        if days_year == 365:
            year_sum = (int(year_n) * 365) + (month_n * 28) + int(day_n)
        else: # если месяц равен 2, 366 дней в году, то умножаем на 29
            year_sum = (int(year_n) * 366) + (month_n * 29) + int(day_n)
    else: # для остальных месяцев умножаем на 30
        year_sum = (int(year_n) * 365) + (month_n * 30) + int(day_n)

# дата рождения:
    if happy_month == 1 or 3 or 5 or 7 or 8 or 10 or 12: # если месяц равен 1, 3, 5, 7, 8, 10 и 12, то умножаем на 31
        year_sum_happy = (int(happy_year) * 365) + (int(happy_month) * 31) + int(happy_day)
    elif happy_month == 2: # если месяц равен 2, то умножаем на 28 если 365 дней в году
        if days_year == 365:
            year_sum_happy = (int(happy_year) * 365) + (int(happy_month) * 28) + int(happy_day)
        else: # если месяц равен 2, 366 дней в году, то умножаем на 29
            year_sum_happy = (int(happy_year) * 366) + (int(happy_month) * 29) + int(happy_day)
    else: # для остальных месяцев умножаем на 30
        year_sum_happy = (int(happy_year) * 365) + (int(happy_month) * 30) + int(happy_day)

    # узнаю разницу и делю её на сколько дней сейчас в году.
    equally = (int(year_sum) - int(year_sum_happy)) / int(days_year)
    # использую округление чтобы отбросить все точки.
    print("Ваш возраст = " + str(round(equally)))

    repeat = input("Посчитать еще? 'нет' для заверщения программы. ")
    if repeat == 'нет':
        break

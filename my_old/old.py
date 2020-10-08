# импорт модуля
import datetime as dt

class MyOld:
    """Класс для расчёта вашего возраста"""

    def instruction(self):
        """Инструкция и меню."""
        print(
            """
    Программа расчитает сколько вам полных лет.
            
    Меню:
    0 - Выход
    1 - Расчитать свой возраст
            """
        )

    def show_menu(self):
        """Функция для передачи значения
        которое выберит пользователь."""

        # вызывает иструкцию и меню.
        self.instruction()

        choice = ''
        while choice != '0':
            choice = input("Ваш выбор - ")
            if choice == '0':
                print("Спасибо что поработали с программой.")
            # если выбрать пункт под №1, то выполниться функция
            # self.item_1 и получит значение под №1
            elif choice == '1':
                self.item_1(choice)
            else:
                print('Простите но такого пункта нет в меню.')


    def item_1(self, choice):
        """Функция которая выполняет первый пукт"""
        if choice == '1':
            # текущая дата
            now = dt.datetime.now().date()
            # Запрашиваю дату рождения
            print("\nНужно ввести дату в формате 1900.11.1")
            date = input('Введите дату своего рождения: ')
            # Делаю список из строки
            y, m, d = date.split('.')
            # превращаю значения в модуль datetime для подсчёта
            date_of_birth = dt.datetime(int(y), int(m), int(d)).date()

            delta = (now - date_of_birth) / 365
            print(f'Вам {delta.days} лет.')



my = MyOld()
my.show_menu()
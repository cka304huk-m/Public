# Счётчик банкнот.
import tkinter

class MyNote:
    def __init__(self):
        self.settings_window()

        self.description_input()

        self.button_()

        self.results()

        self.packing()

        # Запускаю цикл.
        self.main_window.mainloop()

    def settings_window(self):
        # Настройки окна.

        # Создаю главное окно.
        self.main_window = tkinter.Tk()

        # Название окна.
        self.main_window.title('Счётчик банкнот')

        # Размер окна.
        self.main_window.geometry('195x320')

        # Отключаю разворот окна.
        self.main_window.resizable(False, False)

        # Описание в которое положу результат суммирования.
        self.value = tkinter.StringVar()

        # Шрифт и размер.
        self.my_font = 14

    def description_input(self):
        # Описание и ввод рублей.

        # Рамки для описания и ввода купюр.
        self.frame_5000 = tkinter.Frame(self.main_window)
        self.frame_2000 = tkinter.Frame(self.main_window)
        self.frame_1000 = tkinter.Frame(self.main_window)
        self.frame_500 = tkinter.Frame(self.main_window)
        self.frame_200 = tkinter.Frame(self.main_window)
        self.frame_100 = tkinter.Frame(self.main_window)
        self.frame_50 = tkinter.Frame(self.main_window)
        self.frame_10 = tkinter.Frame(self.main_window)
        self.frame_5 = tkinter.Frame(self.main_window)
        self.frame_2 = tkinter.Frame(self.main_window)
        self.frame_1 = tkinter.Frame(self.main_window)

        # Описание 5000 рублей.
        self.label_5000 = tkinter.Label(self.frame_5000,
                                        text='5000: ',
                                        font=self.my_font)
        # Окно для ввода количества 5000 рублей.
        self.entry_5000 = tkinter.Entry(self.frame_5000,
                                        width=15)

        # Описание 2000 рублей.
        self.label_2000 = tkinter.Label(self.frame_2000,
                                        text='2000: ',
                                        font=self.my_font)
        # Окно для ввода количества 2000 рублей.
        self.entry_2000 = tkinter.Entry(self.frame_2000,
                                        width=15)

        # Описание 1000 рублей.
        self.label_1000 = tkinter.Label(self.frame_1000,
                                        text='1000: ',
                                        font=self.my_font)
        # Окно для ввода количества 1000 рублей.
        self.entry_1000 = tkinter.Entry(self.frame_1000,
                                        width=15)

        # Описание 500 рублей.
        self.label_500 = tkinter.Label(self.frame_500,
                                       text='  500: ',
                                       font=self.my_font)
        # Окно для ввода количества 500 рублей.
        self.entry_500 = tkinter.Entry(self.frame_500,
                                       width=15)

        # Описание 200 рублей.
        self.label_200 = tkinter.Label(self.frame_200,
                                       text='  200: ',
                                       font=self.my_font)
        # Окно для ввода количества 200 рублей.
        self.entry_200 = tkinter.Entry(self.frame_200,
                                       width=15)

        # Описание 100 рублей.
        self.label_100 = tkinter.Label(self.frame_100,
                                       text='  100: ',
                                       font=self.my_font)
        # Окно для ввода количества 100 рублей.
        self.entry_100 = tkinter.Entry(self.frame_100,
                                       width=15)

        # Описание 50 рублей.
        self.label_50 = tkinter.Label(self.frame_50,
                                      text='    50: ',
                                      font=self.my_font)
        # Окно для ввода количества 50 рублей.
        self.entry_50 = tkinter.Entry(self.frame_50,
                                      width=15)

        # Описание 10 рублей.
        self.label_10 = tkinter.Label(self.frame_10,
                                      text='    10: ',
                                      font=self.my_font)
        # Окно для ввода количества 50 рублей.
        self.entry_10 = tkinter.Entry(self.frame_10,
                                      width=15)

        # Описание 5 рублей.
        self.label_5 = tkinter.Label(self.frame_5,
                                     text='      5: ',
                                     font=self.my_font)
        # Окно для ввода количества 5 рублей.
        self.entry_5 = tkinter.Entry(self.frame_5,
                                     width=15)

        # Описание 2 рубля.
        self.label_2 = tkinter.Label(self.frame_2,
                                     text='      2: ',
                                     font=self.my_font)
        # Окно для ввода количества 2 рублей.
        self.entry_2 = tkinter.Entry(self.frame_2,
                                     width=15)

        # Описание 1 рубля.
        self.label_1 = tkinter.Label(self.frame_1,
                                     text='      1: ',
                                     font=self.my_font)
        # Окно для ввода количества 1 рублей.
        self.entry_1 = tkinter.Entry(self.frame_1,
                                     width=15)

    def button_(self):
        # Располагаю рамку для кнопки и саму кнопку.

        # Рамка для кнопки посчитать.
        self.button_result_frame = tkinter.Frame(self.main_window)

        # Кнопка показать деньги.
        self.button_result = tkinter.Button(self.button_result_frame,
                                            text='Сумма в кассе', width=18,
                                            command=self.result_summa)

    def results(self):
        # Выводит результаты.

        # Рамка для вывода результата.
        self.frame_result = tkinter.Frame(self.main_window)

        # Описание равное сумме денег.
        self.label_result = tkinter.Label(self.frame_result,
                                          textvariable=self.value,
                                          font=('Arial', 22))

    def packing(self):
        # Упаковываю рамки, кнопки...
        self.frame_5000.pack()
        self.label_5000.pack(side='left')
        self.entry_5000.pack(side='left')

        self.frame_2000.pack()
        self.label_2000.pack(side='left')
        self.entry_2000.pack(side='left')

        self.frame_1000.pack()
        self.label_1000.pack(side='left')
        self.entry_1000.pack(side='left')

        self.frame_500.pack()
        self.label_500.pack(side='left')
        self.entry_500.pack(side='left')

        self.frame_200.pack()
        self.label_200.pack(side='left')
        self.entry_200.pack(side='left')

        self.frame_100.pack()
        self.label_100.pack(side='left')
        self.entry_100.pack(side='left')

        self.frame_50.pack()
        self.label_50.pack(side='left')
        self.entry_50.pack(side='left')

        self.frame_10.pack()
        self.label_10.pack(side='left')
        self.entry_10.pack(side='left')

        self.frame_5.pack()
        self.label_5.pack(side='left')
        self.entry_5.pack(side='left')

        self.frame_2.pack()
        self.label_2.pack(side='left')
        self.entry_2.pack(side='left')

        self.frame_1.pack()
        self.label_1.pack(side='left')
        self.entry_1.pack(side='left')

        self.button_result_frame.pack()
        self.button_result.pack()

        self.frame_result.pack()
        self.label_result.pack()

    def result_summa(self):
        # Результат подсчета.

        if len(self.entry_5000.get()) > 0:
            sum_5000 = float(self.entry_5000.get()) * 5000
        else:
            sum_5000 = 0

        if len(self.entry_2000.get()) > 0:
            sum_2000 = float(self.entry_2000.get()) * 2000
        else:
            sum_2000 = 0

        if len(self.entry_1000.get()) > 0:
            sum_1000 = float(self.entry_1000.get()) * 1000
        else:
            sum_1000 = 0

        if len(self.entry_500.get()) > 0:
            sum_500 = float(self.entry_500.get()) * 500
        else:
            sum_500 = 0

        if len(self.entry_200.get()) > 0:
            sum_200 = float(self.entry_200.get()) * 200
        else:
            sum_200 = 0

        if len(self.entry_100.get()) > 0:
            sum_100 = float(self.entry_100.get()) * 100
        else:
            sum_100 = 0

        if len(self.entry_50.get()) > 0:
            sum_50 = float(self.entry_50.get()) * 50
        else:
            sum_50 = 0

        if len(self.entry_10.get()) > 0:
            sum_10 = float(self.entry_10.get()) * 10
        else:
            sum_10 = 0

        if len(self.entry_5.get()) > 0:
            sum_5 = float(self.entry_5.get()) * 5
        else:
            sum_5 = 0

        if len(self.entry_2.get()) > 0:
            sum_2 = float(self.entry_2.get()) * 2
        else:
            sum_2 = 0

        if len(self.entry_1.get()) > 0:
            sum_1 = float(self.entry_1.get()) * 1
        else:
            sum_1 = 0

        amount = sum_5000 + sum_2000 + sum_1000 + \
            sum_500 + sum_200 + sum_100 + sum_50 + \
            sum_10 + sum_5 + sum_2 + sum_1

        self.value.set(f'₽ {amount:,.0f} ')

# Создаю экземпляр.
if __name__ == '__main__':
    note = MyNote()

# Расчёт заработной платы.

import tkinter, datetime, os
from PIL import ImageGrab

class MySalary:
    def __init__(self):
        # Создать виджет главного окна.
        self.main_window = tkinter.Tk()

        self.settingsWindow()

        self.font_results = 'Arial', 22

        # Переменная для сохранения даты и времени
        self.value_data = tkinter.StringVar()

        # Переменная для подсчёта зп
        self.value_accrued = tkinter.StringVar()

        # Переменная для сохранения аванса + товара
        self.value_prePP = tkinter.StringVar()

        # Переменная для сохранения НДФЛ.
        self.value_ndfl = tkinter.StringVar()

        # Переменная к выдаче.
        self.value_all = tkinter.StringVar()

        self.dataStr()
        self.frameEnterSalary()
        self.frameEnterWatch()
        self.hoursWork()
        self.premium()
        self.prepayment()
        self.results()
        self.buttonFrame_print()
        self.accruedEnter()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    def settingsWindow(self):
        # Показать заголовок.
        self.main_window.title('Посчитать зарплату')
        self.main_window.geometry("300x500")
        self.main_window.resizable(False, False)

    def dataStr(self):
        # Создаю рамку в котором будет размещаться оклад
        self.frame_dataStr = tkinter.Frame(self.main_window)

        # Получаю текущую дату и время.
        now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

        # Устанавливаю значения, даты и времени.
        self.value_data.set(now)

        # Вывожу описание.
        self.label_salary = tkinter.Label(self.frame_dataStr,
                                          text='Расчёт зарплаты на ')

        # Вывожу текущую дату и время.
        self.label_data = tkinter.Label(self.frame_dataStr,
                                        textvariable=self.value_data)

        # Упаковываю их.
        self.frame_dataStr.pack()
        self.label_salary.pack(side='left')
        self.label_data.pack(side='left')

    def print_salary(self):
        # Получаю координаты точек х и y.
        x = self.main_window.winfo_x()
        y = self.main_window.winfo_y()
        # Получаю высоту и ширину формы.
        height = self.main_window.winfo_height()
        width = self.main_window.winfo_width()
        # Делаем снимок, сохраняем и печатаем.
        image = ImageGrab.grab( (x, y, x+width, y+height) )
        image.save("screen.png", "PNG")
        os.startfile("screen.png", "print")

    def buttonFrame_print(self):
        # Рамка для кнопки распечатать.
        self.frame_print = tkinter.Frame(self.main_window)

        # Кнопка распечатать
        self.print_sal_button = tkinter.Button(self.frame_print,
                                               text='Распечатать зарплату',
                                               width=34,
                                               command=self.print_salary)

        # Упаковываю рамку и кнопку.
        self.frame_print.pack()
        self.print_sal_button.pack()

    def frameEnterSalary(self):
        # Ввод данных для расчёта заработной платы.

        # Создаю рамку c расположением описание и поля ввода данных.
        self.frameEnterData = tkinter.Frame(self.main_window)

        self.labelSalary = tkinter.Label(self.frameEnterData,
                                         text=f"{'Оклад':26}")
        self.entrySalary = tkinter.Entry(self.frameEnterData)

        # Упаковывываю рамку, виджеты...
        self.frameEnterData.pack()
        self.labelSalary.pack(side='left')
        self.entrySalary.pack(side='left')

    def frameEnterWatch(self):
        # Описание и ввод рабочих часов.

        # Создаю рамку ввода количества часов.
        self.frame_watch = tkinter.Frame(self.main_window)

        # Описание кол-во раб. часов.
        self.work_watch = tkinter.Label(self.frame_watch,
                                        text=f'{"Кол-во раб. часов":19}')

        # Ввод кол-во раб. часов
        self.enter_workWatch = tkinter.Entry(self.frame_watch)

        # Упаковывываю рамку, виджеты...
        self.frame_watch.pack()
        self.work_watch.pack(side='left')
        self.enter_workWatch.pack(side='left')

    def hoursWork(self):
        # Число отработанных часов.

        # рамка для ввода кол-во отработых часов.
        self.frameHoursWork = tkinter.Frame(self.main_window)

        # описание отработано часов.
        self.labelHoursWork = tkinter.Label(self.frameHoursWork,
                                            text=f'{"Отработано часов":17}')

        # поле ввода отработаных часов.
        self.entryHoursWork = tkinter.Entry(self.frameHoursWork)

        # Упаковываю рамку, виджеты...
        self.frameHoursWork.pack()
        self.labelHoursWork.pack(side='left')
        self.entryHoursWork.pack(side='left')

    def accruedEnter(self):
        # Вывод примерной зарплаты.

        # Рамка для вывода зарплаты без премии.
        self.frameAccrued = tkinter.Frame(self.main_window)

        self.labelAccrued = tkinter.Label(self.frameAccrued,
                                          text=f'{"Всего начислено:"}',
                                          font=self.font_results)


        self.label_results = tkinter.Label(self.frameAccrued,
                                           textvariable=self.value_accrued,
                                           font=self.font_results)

        self.labelPrePr = tkinter.Label(self.frameAccrued,
                                          text=f'{"Аванс + товар:"}',
                                          font=self.font_results)

        self.label_results2 = tkinter.Label(self.frameAccrued,
                                           textvariable=self.value_prePP,
                                           font=self.font_results)

        self.label_ndfl = tkinter.Label(self.frameAccrued,
                                        text='Удержан НДФЛ:',
                                        font=self.font_results)

        self.label_results3 = tkinter.Label(self.frameAccrued,
                                            textvariable=self.value_ndfl,
                                            font=self.font_results)

        self.labelToIssue = tkinter.Label(self.frameAccrued,
                                          text='К выдаче:',
                                          font=self.font_results)

        self.label_results4 = tkinter.Label(self.frameAccrued,
                                            textvariable=self.value_all,
                                            font=self.font_results)

        # Упаковываю рамки виджеты.
        self.frameAccrued.pack()
        self.labelAccrued.pack()
        self.label_results.pack()
        self.labelPrePr.pack()
        self.label_results2.pack()
        self.label_ndfl.pack()
        self.label_results3.pack()
        self.labelToIssue.pack()
        self.label_results4.pack()

    def premium(self):
        # Ввод премии.

        # Рамка где расположу описание ввод премии.
        self.framePremium = tkinter.Frame(self.main_window)

        # описание премия.
        self.label_premium = tkinter.Label(self.framePremium,
                                           text=f'{"Премия":25}')

        # окно ввода премии.
        self.entry_premium = tkinter.Entry(self.framePremium)

        # Упаковываю рамку и вилжеты.
        self.framePremium.pack()
        self.label_premium.pack(side='left')
        self.entry_premium.pack(side='left')

    def prepayment(self):
        # Аванс + товар.

        # Рамка для описания и ввода аванса и товара.
        self.prepayment_product = tkinter.Frame(self.main_window)

        # Описание Аванс + товар.
        self.labelpreProduct = tkinter.Label(self.prepayment_product,
                                             text=f'{"Аванс + товар":20}')

        self.entryPproduct = tkinter.Entry(self.prepayment_product)

        # Упаковываю рамку и виджеты.
        self.prepayment_product.pack()
        self.labelpreProduct.pack(side='left')
        self.entryPproduct.pack(side='left')

    def results(self):
        # рамка для подсчета зп.
        self.results_frame = tkinter.Frame(self.main_window)

        # кнопка зп с премией.
        self.results_button_premium = tkinter.Button(self.results_frame,
                                             text='Зарплата без НДФЛ',
                                             command=self.calc_salary_premium_prepayment_no_ndfl)

        self.results_button_premium2 = tkinter.Button(self.results_frame,
                                                     text='Зарплата с НДФЛ',
                                                     command=self.calc_salary_premium_prepayment_ndfl)

        # упаковываю рамку, кнопку и виджеты.
        self.results_frame.pack()
        self.results_button_premium.pack(side='left')
        self.results_button_premium2.pack(side='left')

    def calc_salary_premium_prepayment_no_ndfl(self):
        # зп с вычитом аванса и товара, но без ндфл.

        salary = float(self.entrySalary.get())

        workWatch = float(self.enter_workWatch.get())

        hoursWork = float(self.entryHoursWork.get())

        if len(self.entry_premium.get()) > 0:
            premium = float(self.entry_premium.get())
        else:
            premium = 0

        if len(self.entryPproduct.get()) > 0:
            prepayment = float(self.entryPproduct.get())
        else:
            prepayment = 0

        results2 = ((salary / workWatch) * hoursWork) + premium - prepayment

        results1 = ((salary / workWatch) * hoursWork) + premium

        self.value_accrued.set(f'₽ {results1:.0f}')

        self.value_prePP.set(f'₽ {prepayment:.0f}')

        self.value_ndfl.set(f'₽ 0')

        self.value_all.set(f'₽ {results2:.0f}')

    def calc_salary_premium_prepayment_ndfl(self):
        # зп с вычитом аванса и товара, но без ндфл.

        salary = float(self.entrySalary.get())

        workWatch = float(self.enter_workWatch.get())

        hoursWork = float(self.entryHoursWork.get())

        if len(self.entry_premium.get()) > 0:
            premium = float(self.entry_premium.get())
        else:
            premium = 0

        if len(self.entryPproduct.get()) > 0:
            prepayment = float(self.entryPproduct.get())
        else:
            prepayment = 0

        ndfl = 3600

        results2 = ((salary / workWatch) * hoursWork) + premium - prepayment - ndfl

        results1 = ((salary / workWatch) * hoursWork) + premium

        self.value_accrued.set(f'₽ {results1:.0f}')

        self.value_prePP.set(f'₽ {prepayment:.0f}')

        self.value_ndfl.set(f'₽ {ndfl:.0f}')

        self.value_all.set(f'₽ {results2:.0f}')

# Создать экземпляр класса MySalary.
if __name__ == '__main__':
    my_salary = MySalary()

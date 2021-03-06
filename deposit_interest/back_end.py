# калькулятор расчёта процентов по вкладу

class DepositCalculator:
    """Калькулятор депозита"""

    def __init__(self, deposit, interest_rate, days, days_year):
        """Инициализирую атрибуты"""
        self.deposit = deposit # Сумма депозита
        self.interest_rate = interest_rate # Процентная ставка, годовых
        self.days = days # На сколько дней
        self.days_year = days_year # Сколько дней в году

    def my_deposit(self):
        """Считывает мой депозит"""
        return self.deposit

    def percent(self):
        """Высчитывает процент от вклада, без реинвестирования"""
        sum = (float(self.deposit) * int(self.interest_rate) * int(self.days)) / (int(self.days_year) * 100)
        sum = float('{:.3}'.format(sum))
        return sum

    def all_sum(self):
        """Сложения депозита и дохода"""
        am = float(self.percent()) + int(self.my_deposit())
        return am

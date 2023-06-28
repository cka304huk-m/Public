# Конвертирования названия месяца в число.

def edit_month(month):
    if month == 'января':
        digMonth = '01'
    elif month == 'февраля':
        digMonth = '02'
    elif month == 'марта':
        digMonth = '03'
    elif month == 'апреля':
        digMonth = '04'
    elif month == 'мая':
        digMonth = '05'
    elif month == 'июня':
        digMonth = '06'
    elif month == 'июля':
        digMonth = '07'
    elif month == 'августа':
        digMonth = '08'
    elif month == 'сентября':
        digMonth = '09'
    elif month == 'октября':
        digMonth = '10'
    elif month == 'ноября':
        digMonth = '11'
    elif month == 'декабря':
        digMonth = '12'
    return digMonth
import openpyxl
from find_code import *
from converter import converter

def main():
    try:
        # Если файл имеет расширения не .xlsx, то сохраняю его в этот формат.
        converter()
    except:
        # Иначе пропустить.
        pass

    create_document()

def create_document():
    upd = openpyxl.open('upd.xlsx')
    sheet = upd.active

    numberDocument = sheet['B17'].value[17:24].strip()  # номер документа
    data = sheet['B17'].value[27:].split()  # Дата
    if len(data[0]) > 1:
        day = data[0]   # День
    else:
        day = f'0{data[0]}'  # День
    month = FC.edit_month(data[1]) # Месяц
    year = data[2]  # Год
    data_document = f'{day}/{month}/{year}'

    inn = '9201002117'
    comment = '=)'

    one_string = f'{numberDocument};{data_document};;;{inn};;;;;;;;;;;{comment};'

    print('Ожидайте, сейчас происходит магия =)')

    with open('tdm.txt', 'w') as new_file:
        new_file.write(one_string + '\n')
        for row in range(25, sheet.max_row + 1):
            if sheet[row][3].value != None:
                if 'SQ' in sheet[row][3].value[:2]:
                    n = FindCode(sheet[row][3].value)
                    new_code = n.find_tdm()
                    new_string = f';{new_code};;;;;;{sheet[row][50].value};;;{sheet[row][60].value};'
                    new_file.write(new_string + '\n')
                elif len(sheet[row][3].value) == 5:
                    n = FindCode(sheet[row][3].value)
                    new_code = n.find_fortisflex()
                    new_string = f';{new_code};;;;;;{sheet[row][50].value * 100};;;{sheet[row][60].value / 100};'
                    new_file.write(new_string + '\n')
                else:
                    new_string = f';{sheet[row][3].value};;;;;;{sheet[row][50].value};;;{sheet[row][60].value};'
                    new_file.write(new_string + '\n')

    print('\nВсе готово!')

if __name__ == '__main__':
    main()